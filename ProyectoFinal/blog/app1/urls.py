from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('registro/', views.registro, name = "registro"),
    path('login/', views.login_view, name = "login"),
    path('loginExitoso/', views.inicio_logueado, name = "loginExitoso"),
    path('perfil/', views.perfil, name = "perfil"),
    path('provincias/', views.provincias, name = "provincias"),
    path('excursiones/', views.provincias, name = "excursiones"), #Redirecciona intencionalmente a Provincia con el fin de que seleccione el lugar turistico
    path('gastronomia/', views.provincias, name = "gastronomia"), #Redirecciona intencionalmente a Provincia con el fin de que seleccione el lugar turistico
    path('viajes/', views.viajes, name = "viajes"),
    path('about/', views.about, name = "about"),
    path('inicio_logueado/', views.inicio_logueado, name = "inicio_logueado"),
    path('obligatorio/', views.obligatorio, name = "obligatorio"),
    path('buenos_aires/', views.buenos_aires, name = "buenos_aires"),
    path('mendoza/', views.mendoza, name = "mendoza"),
    path('rio_negro/', views.rio_negro, name = "rio_negro"),
    path('no_hay_pagina_aun/', views.no_hay_pagina_aun, name = "no_hay_pagina_aun"),
    #path('registro_exitoso/', views.registro_exitoso, name = "registro_exitoso"),
]

