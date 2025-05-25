# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # cuando entre a /
    path('panel-admin/', views.panel_administracion, name='panel_administracion'),
    path('contacto/', views.contacto, name='contacto'),
    path('mensajes/', views.vista_mensajes, name='vista_mensajes'),  # Nueva URL
    path('marcar-leido/<int:mensaje_id>/', views.marcar_leido, name='marcar_leido'),  # Para toggle leído/no leído
    path('api/', views.api_home, name='api'),

    
    
]