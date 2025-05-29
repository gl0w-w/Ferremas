from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UsuarioSerializer, LoginSerializer
from .serializers import UsuarioListaSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from .models import Usuario
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from carro_compras.models import Venta
from django.utils import timezone
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from usuarios.serializers import UsuarioSerializer as UsuarioCompleto
from .serializers import UsuarioSerializer as CarroUsuario
# Importaciones para Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

def iniciosesion(request):
    return render(request, 'usuarios/iniciosesion.html')
def registro(request):
    return render(request, 'usuarios/registro.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('/')

class RegistroAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Registra un nuevo usuario en el sistema y genera un token de autenticación",
        operation_summary="Registrar nuevo usuario",
        tags=['Autenticación'],
        request_body=UsuarioSerializer,
        responses={
            201: openapi.Response(
                'Usuario registrado exitosamente',
                openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'status': openapi.Schema(type=openapi.TYPE_STRING, description='Estado de la operación'),
                        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Mensaje de confirmación'),
                        'token': openapi.Schema(type=openapi.TYPE_STRING, description='Token de autenticación'),
                        'redirect_url': openapi.Schema(type=openapi.TYPE_STRING, description='URL de redirección')
                    }
                )
            ),
            400: 'Datos inválidos o error de validación'
        }
    )
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'status': 'success',
                'message': 'Usuario registrado exitosamente',
                'token': token.key,
                'redirect_url': '/'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Autentica un usuario existente y genera un token de sesión",
        operation_summary="Iniciar sesión",
        tags=['Autenticación'],
        request_body=LoginSerializer,
        responses={
            200: openapi.Response(
                'Inicio de sesión exitoso',
                openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'status': openapi.Schema(type=openapi.TYPE_STRING, description='Estado de la operación'),
                        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Mensaje de confirmación'),
                        'token': openapi.Schema(type=openapi.TYPE_STRING, description='Token de autenticación'),
                        'redirect_url': openapi.Schema(type=openapi.TYPE_STRING, description='URL de redirección')
                    }
                )
            ),
            400: 'Credenciales inválidas o error de validación'
        }
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'status': 'success',
                'message': 'Inicio de sesión exitoso',
                'token': token.key,
                'redirect_url': '/'
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@swagger_auto_schema(
    method='get',
    operation_description="Obtiene la lista completa de usuarios registrados (solo administradores)",
    operation_summary="Listar todos los usuarios",
    tags=['Usuarios - Admin'],
    responses={
        200: openapi.Response('Lista de usuarios', UsuarioListaSerializer(many=True)),
        403: 'No autorizado - Solo administradores',
        500: 'Error interno del servidor'
    }
)
@api_view(['GET'])
@permission_classes([IsAdminUser])
def api_lista_usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioListaSerializer(usuarios, many=True)
    return Response(serializer.data)    

@user_passes_test(lambda u: u.is_staff)
def vista_lista_usuarios(request):
    return render(request, 'usuarios/lista_usuarios.html')

@user_passes_test(lambda u: u.is_staff, login_url='/usuarios/iniciosesion/')
def vista_agregar_usuario(request):
    return render(request, 'usuarios/agregar_usuario.html')


@swagger_auto_schema(
    method='post',
    operation_description="Crea un nuevo usuario en el sistema (solo administradores)",
    operation_summary="Crear usuario",
    tags=['Usuarios - Admin'],
    request_body=UsuarioSerializer,
    responses={
        201: openapi.Response('Usuario creado exitosamente', UsuarioSerializer),
        400: 'Datos inválidos o error de validación',
        403: 'No autorizado - Solo administradores'
    }
)
@api_view(['POST'])
@permission_classes([IsAdminUser])
def api_agregar_usuario(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)    

@swagger_auto_schema(
    method='patch',
    operation_description="Activa o desactiva un usuario. Los administradores no pueden suspender su propia cuenta",
    operation_summary="Activar/Desactivar usuario",
    tags=['Usuarios - Admin'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID del usuario", type=openapi.TYPE_INTEGER, required=True)
    ],
    responses={
        200: openapi.Response(
            'Estado actualizado correctamente',
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING, description='Mensaje de confirmación'),
                    'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Nuevo estado del usuario')
                }
            )
        ),
        403: 'No autorizado o intento de auto-suspensión',
        404: 'Usuario no encontrado'
    }
)
@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def api_toggle_activo_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if usuario == request.user:
        return Response(
            {"error": "No puedes suspender tu propia cuenta."},
            status=403
        )

    usuario.is_active = not usuario.is_active
    usuario.save()
    return Response({"message": "Estado actualizado", "is_active": usuario.is_active})

@user_passes_test(lambda u: u.is_staff)
def vista_editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario})


@swagger_auto_schema(
    method='put',
    operation_description="Edita los datos de un usuario existente. No se puede editar usuarios suspendidos ni la propia cuenta",
    operation_summary="Editar usuario",
    tags=['Usuarios - Admin'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID del usuario a editar", type=openapi.TYPE_INTEGER, required=True)
    ],
    request_body=UsuarioSerializer,
    responses={
        200: openapi.Response('Usuario actualizado exitosamente', UsuarioSerializer),
        400: 'Datos inválidos o error de validación',
        403: 'No autorizado, usuario suspendido o intento de auto-edición',
        404: 'Usuario no encontrado'
    }
)
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def api_editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    # 🚫 No permitir editar usuarios suspendidos
    if not usuario.is_active:
        return Response({"error": "No puedes editar un usuario suspendido."}, status=status.HTTP_403_FORBIDDEN)

    # 🚫 No permitir editarse a uno mismo
    if request.user == usuario:
        return Response({"error": "No puedes editar tu propia cuenta desde el panel."}, status=status.HTTP_403_FORBIDDEN)

    serializer = UsuarioSerializer(usuario, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VistaRecuperarConValidacion(PasswordResetView):
    template_name = 'usuarios/recuperar.html'
    email_template_name = 'usuarios/password_reset_email.html'
    subject_template_name = 'usuarios/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        Usuario = get_user_model()
        if not Usuario.objects.filter(email=email).exists():
            messages.error(self.request, "El correo ingresado no está registrado.")
            return self.form_invalid(form)
        return super().form_valid(form)