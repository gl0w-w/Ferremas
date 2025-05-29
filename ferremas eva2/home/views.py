# home/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from productos.models import Producto
from .models import Contacto

def index(request):
    productos_destacados = Producto.objects.all().order_by('-id')[:3]  # los 3 más recientes
    return render(request, 'home/index.html', {'productos_destacados': productos_destacados})

@user_passes_test(lambda u: u.is_staff, login_url='/usuarios/iniciosesion/')
def panel_administracion(request):
    # Obtener mensajes de contacto para mostrar estadísticas
    mensajes_no_leidos = Contacto.objects.filter(leido=False).count()
    
    context = {
        'mensajes_no_leidos': mensajes_no_leidos,
    }
    return render(request, 'home/panel_admin.html', context)

@user_passes_test(lambda u: u.is_staff, login_url='/usuarios/iniciosesion/')
def vista_mensajes(request):
    # Obtener todos los mensajes ordenados por fecha (más recientes primero)
    mensajes = Contacto.objects.all().order_by('-fecha_creacion')
    
    # Filtros opcionales
    filtro_estado = request.GET.get('estado', 'todos')
    busqueda = request.GET.get('busqueda', '')
    
    if filtro_estado == 'no_leidos':
        mensajes = mensajes.filter(leido=False)
    elif filtro_estado == 'leidos':
        mensajes = mensajes.filter(leido=True)
    
    if busqueda:
        mensajes = mensajes.filter(
            asunto__icontains=busqueda
        ) | mensajes.filter(
            usuario__first_name__icontains=busqueda
        ) | mensajes.filter(
            usuario__last_name__icontains=busqueda
        )
    
    # Paginación (10 mensajes por página)
    paginator = Paginator(mensajes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Estadísticas
    total_mensajes = Contacto.objects.count()
    mensajes_no_leidos = Contacto.objects.filter(leido=False).count()
    mensajes_leidos = Contacto.objects.filter(leido=True).count()
    
    context = {
        'page_obj': page_obj,
        'total_mensajes': total_mensajes,
        'mensajes_no_leidos': mensajes_no_leidos,
        'mensajes_leidos': mensajes_leidos,
        'filtro_estado': filtro_estado,
        'busqueda': busqueda,
    }
    
    return render(request, 'home/vista_mensajes.html', context)

@user_passes_test(lambda u: u.is_staff, login_url='/usuarios/iniciosesion/')
def marcar_leido(request, mensaje_id):
    if request.method == 'POST':
        mensaje = get_object_or_404(Contacto, id=mensaje_id)
        mensaje.leido = not mensaje.leido  # Toggle del estado
        mensaje.save()
        
        estado = "leído" if mensaje.leido else "no leído"
        messages.success(request, f'Mensaje marcado como {estado}.')
    
    return redirect('vista_mensajes')

def contacto(request):
    # Inicializar contexto
    context = {}
    
    # Si el usuario está autenticado, obtener sus mensajes
    if request.user.is_authenticated:
        mensajes_usuario = Contacto.objects.filter(
            usuario=request.user
        ).order_by('-fecha_creacion')[:5]  # Los 5 más recientes
        
        context['mensajes_usuario'] = mensajes_usuario
    
    if request.method == 'POST':
        # Verificar que el usuario esté autenticado
        if not request.user.is_authenticated:
            messages.error(request, 'Debes iniciar sesión para enviar un mensaje.')
            return redirect('contacto')
        
        # Obtener datos del formulario
        asunto = request.POST.get('asunto', '').strip()
        mensaje = request.POST.get('mensaje', '').strip()
        
        # Validar que los campos no estén vacíos
        if not asunto or not mensaje:
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'home/contacto.html', context)
        
        # Crear el mensaje de contacto
        try:
            Contacto.objects.create(
                usuario=request.user,
                asunto=asunto,
                mensaje=mensaje
            )
            messages.success(request, '¡Tu mensaje ha sido enviado exitosamente! Te responderemos pronto.')
            return redirect('contacto')
        except Exception as e:
            messages.error(request, 'Ha ocurrido un error al enviar tu mensaje. Por favor, inténtalo de nuevo.')
            return render(request, 'home/contacto.html', context)
    
    return render(request, 'home/contacto.html', context)

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def api_home(request):
    return render(request, 'home/apis.html')  

def swagger_docs(request):
    """Vista para mostrar la documentación de Swagger"""
    return render(request, 'home/swagger.html')