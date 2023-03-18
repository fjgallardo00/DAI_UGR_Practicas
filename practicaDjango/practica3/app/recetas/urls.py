# recetas/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from . import views

urlpatterns = [
    path('inicio', views.index, name='index'),
    path('', views.index, name='index'),
    path('modo', views.modo, name='modo'),
    path('buscar', views.buscar, name='buscar'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', include('django.contrib.auth.urls')),
    path('mostrar_receta/<int:id>', views.mostrar_receta, name='mostrar_receta'),
    path('mostrar_receta', views.mostrar_receta, name='mostrar_receta'),
    path('eliminar_receta/<int:id>', views.eliminar_receta, name='eliminar_receta'),
    path('eliminar_receta', views.eliminar_receta, name='eliminar_receta'),
    path('editar_receta/<int:id>', views.editar_receta, name='editar_receta'),
    path('editar_receta', views.editar_receta, name='editar_receta'),
    path('add_receta', views.add_receta, name='add_receta'),
    path('formulario/<int:id>', views.formulario, name='formulario'),
    path('formulario', views.formulario, name='formulario'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
