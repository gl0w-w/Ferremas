# home/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Contacto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    asunto = models.CharField(max_length=200, verbose_name='Asunto')
    mensaje = models.TextField(verbose_name='Mensaje')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    leido = models.BooleanField(default=False, verbose_name='Leído')
    
    class Meta:
        verbose_name = 'Mensaje de Contacto'
        verbose_name_plural = 'Mensajes de Contacto'
        ordering = ['-fecha_creacion']  # Los más recientes primero
    
    def __str__(self):
        return f"{self.asunto} - {self.usuario.get_full_name()} ({self.fecha_creacion.strftime('%d/%m/%Y %H:%M')})"