"""
URL configuration for MIWEB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_principal, name="index"),
    path('who', views.pagina_who, name="who"),
    path('Testimonios', views.pagina_testimonios, name="Testimonios"),
    path('Adopta', views.pagina_adopta, name="Adopta"),
    path('registrate', views.pagina_registro, name="registrate"),
    path('exit', views.pagina_exit, name="salida"),
    path('ingresar', views.pagina_ingresar, name="ingresar"),
    path('indexautenticado', views.pagina_indexautenticado, name="indexautenticado"),
    path('donacion', views.donacion, name="donacion"),
    path('testimonio', views.testimonios, name="testimonio")
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

