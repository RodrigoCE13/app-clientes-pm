"""
URL configuration for appclientes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import redirect
from clientes import views as clientes_views
from core import views as core_views
from usuarios import views as usuarios_views
from .decorators import admin_only
#

urlpatterns = [
    path('',lambda request: redirect('signin'), name='root'),
    path('admin/', admin.site.urls),
    path('home/',core_views.home, name='home'),  

    path('clientes/',clientes_views.clientes, name='clientes'),
    path('clientes/create/',admin_only(clientes_views.create_clientes), name='crear_clientes'),
    path('clientes/<int:cliente_id>/',admin_only(clientes_views.cliente_detail), name='cliente_detail'),
    path('clientes/<int:cliente_id>/delete',admin_only(clientes_views.cliente_delete), name='cliente_delete'),
    path('clientes/ver/<int:cliente_id>/', clientes_views.ver_cliente, name="ver_cliente"),

    path('usuarios/',admin_only(usuarios_views.usuarios) , name='usuarios'),
    path('usuarios/create/',admin_only(usuarios_views.registrar_usuarios), name='registrar_usuarios'),
    path('usuarios/<int:usuario_id>/',admin_only(usuarios_views.usuario_detail), name='usuario_detail'),
    path('usuarios/<int:usuario_id>/delete',admin_only(usuarios_views.usuario_delete), name='usuario_delete'),
    path('usuarios/<int:usuario_id>/desactive',admin_only(usuarios_views.desactivar_usuario), name='desactivar_usuario'),
    path('usuarios/<int:usuario_id>/active',admin_only(usuarios_views.activar_usuario), name='activar_usuario'),

    path('logout/',core_views.signout, name='logout'),
    path('signin/',core_views.signin, name='signin'),
]
