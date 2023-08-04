from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
#from django.http import HttpResponse

#Menú Principal
def inicio(request):
    return render(request, "app1/inicio.html")

#Registro
def registro(request):

    if request.method == 'POST':
        miFormulario = RegistroFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            usuario = UserProfile(nickname=informacion['nickname'], 
                                  first_name=informacion['first_name'],
                                  last_name=informacion['last_name'],
                                  email=informacion['email'],
                                  password=informacion['password']
                                  )
            usuario.save()
            
            return render(request, "app1/registro_exitoso.html")
    else:
        miFormulario = RegistroFormulario()

    return render(request, "app1/registro.html", {"miFormulario":miFormulario})            


#Perfil
def perfil(request):
    return render(request, "app1/perfil.html")

#Provincias
def provincias(request):
    return render(request, "app1/provincias.html")

#Viajes
def viajes(request):
    return render(request, "app1/viajes.html")

#excursiones
def excursiones(request):
    return render(request, "app1/excursiones.html")

#Gastronomia
def gastronomia(request):
    return render(request, "app1/gastronomia.html")

#About
def about(request):
    return render(request, "app1/about.html")

#Inicio Logueado
def inicio_logueado(request):
    return render(request, "app1/inicio_logueado.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'app1/inicio.html', {'mensaje': f"Bienvenido {user.username}"})
    else:
        form = AuthenticationForm()

    return render(request, 'app1/login.html', {'form': form})

def obligatorio(request):
    return render(request, "app1/obligatorio.html")

def buenos_aires(request):
    return render(request, "app1/buenos_aires.html")

def mendoza(request):
    return render(request, "app1/mendoza.html")

def rio_negro(request):
    return render(request, "app1/rio_negro.html")

def no_hay_pagina_aun(request): #Agregar en las provincias de la 4 a la 9
    return render(request, "app1/no_hay_pagina_aun.html")

def coment_box(request): #para meter en viaje y en la hoja de las provincias #En models esta el class pero podemos hacer otro porque lo agarre de x ahi
    comments = coment_box.objects.all()
    return render(request, 'viajes.html', {'comments': comments}) 