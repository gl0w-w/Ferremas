# home/admin.py
from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'usuario', 'fecha_creacion', 'leido')
    list_filter = ('leido', 'fecha_creacion')
    search_fields = ('asunto', 'usuario__username', 'usuario__first_name', 'usuario__last_name')
    readonly_fields = ('fecha_creacion',)
    list_editable = ('leido',)
    date_hierarchy = 'fecha_creacion'
    
    fieldsets = (
        ('Información del Mensaje', {
            'fields': ('usuario', 'asunto', 'mensaje', 'fecha_creacion')
        }),
        ('Estado', {
            'fields': ('leido',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('usuario')
    
    # Acción personalizada para marcar como leído
    def marcar_como_leido(self, request, queryset):
        updated = queryset.update(leido=True)
        self.message_user(request, f'{updated} mensajes marcados como leídos.')
    marcar_como_leido.short_description = "Marcar mensajes seleccionados como leídos"
    
    # Acción personalizada para marcar como no leído
    def marcar_como_no_leido(self, request, queryset):
        updated = queryset.update(leido=False)
        self.message_user(request, f'{updated} mensajes marcados como no leídos.')
    marcar_como_no_leido.short_description = "Marcar mensajes seleccionados como no leídos"
    
    actions = ['marcar_como_leido', 'marcar_como_no_leido']