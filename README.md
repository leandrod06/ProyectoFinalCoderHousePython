# Proyecto Final Coder House - Python
#### Comisión: 54955
#### Alumnos:
#Leandro Dramis
#Juan Pablo Apecetche

## Nombre del Proyecto
Argentravel

## Versión
1.0

## Descripción del Proyecto
Página Web destinada a brindar la mayor información posible al viajero que quiera visitar distintos lugares turisticos de Argentina.

##¿Cómo se usa?
1. Ubicarse en la carpeta desde una terminal y ejecutar el servidor con el comando 'python manage.py runserver'
2. Ingresar al server brindado por IP.
3. Contará con 2 comandos para agregar a la url de IP para poder navegar:
- /app1/
- /admin

Nota: la carpeta "App2" fue eliminada.

## Distintas pantallas del sitio:
Desde "/app1/" podrá ingresar al menú principal del sitio donde contara con un resumen de la información que podrá encontrar dentro del site. Este menú le permitirá navegar e ingresar a (siempre agregando "/app1/" adelante): 
- /obligatorio/ - EL CUAL NOS OBLIGA A INICIAR SESIÓN PARA PODER NAVEGAR POR EL SITIO, SALVO POR LA SECCIÓN "/about/".
  
- /registro/ - PARA REGISTRARSE EN EL SITIO.
- /login/ - PARA INICIAR SESIÓN EN EL SITIO.
- /logout/ - PARA CERRAR SESIÓN.

- /perfil/ - PARA INGRESAR AL PERFIL DE LA CUENTA LOGUEADA.
- /eliminarCuenta/ - PARA CONFIRMAR LA ELIMINACIÓN DE LA CUENTA.
- /cuentaEliminada/ - CONFIRMACIÓN DE CUENTA ELIMINADA.
  
- /provincias/ - PARA INGRESAR A LAS DISTINTAS PROVINCIAS CON LAS QUE CUENTA EL SITIO.
- /opiniones/ - PARA INGRESAR A LA SECCIÓN DE OPINIONES DEL SITIO.

- /about/ - PARA SABER SOBRE LA WEB Y SUS CREADORES.
- /no_hay_pagina_aun/ - PANTALLA QUE MOSTRAMOS EN LAS SECCIONES QUE AÚN NO SE MOSTRARON.

## Primeros pasos:
A fin de navegar por las secciones de la página web, se requiere que el usuario inicie sesión o se registre si no cuenta con un perfil creado. 
Una vez registrado, podrá iniciar sesión, que le permitirá navegar por las distintas pantallas mencionadas anteriormente.

## ¿Que se puede hacer en el sitio?
Los usuarios pueden realizar las siguientes accciones:
- Iniciar sesión y navegar por las distintas provincias que poseen opiniones de sus puntos turisticos (actualmente nos encontramos con 3 provincias en funcionamiento, 6 construyendose y las restantes serán agregadas en un futuro).
- Editar el perfil de Usuario y su avatar.
- Cambiar la contraseña de Usuario.
- Eliminar cuenta.
- Cerrar Sesión.

##/admin 
Allí podrán loguearse e ingresar como administrador, donde tendrán permisos para:
- Acceder a paneles de administrador
- Crear nuevos usuarios
- Crear nuevos datos en la BBDD

## Usuarios
Los superusuarios son los siguientes:
#Usuario 1:
- Usuario: admin
- Contraseña: 123456

#Usuario 2:
- Usuario: admin3
- Contraseña: 123456

## Pruebas Realizadas

Ver archivo titulado "Tests Proyecto Argentravel Python.xlsx".

## ¿Que hizo cada integrante?
Las tareas fueron rotandose y nos complementamos mucho. De tal forma, que:
# Leandro:
- Realizó las configuraciones base y creación de archivos para el inicio del proyecto, app1 y templates.
- Modelos de provincia y opiniones, estructura de la web y linkeo de htmls.
- Armado de readme.

# Juan Pablo:
- Diseño de registro, login y logout de usuario (modelo, views, etc).
- Correcciones de html.
- Test de funcionamiento de registro, inicio de sesión, cierre de sesión, opiniones, edición de opiniones.
- CRUD de usuario en la sección "Perfil".

Nota: El armado del formulario de opiniones dio algunas demoras, pero entre ambos pudimos lograr su funcionamiento. Nos hubiera gustado darle un mejor funcionamiento o código mas prolijo, pero no se logró tal resultado eficiente.

Nota2: En una correccion de ultimo momento del funcionamiento del boton de Eliminar cuenta, dejo de funcionar el seteo de Avatar desde "Perfil". Previo a esto, funcionaba. Si se asigna un avatar desde /admin/, se ve la implementacion en el frontend. Sospechamos que el problema del boton para cambiar el avatar tiene que ver con las definiciones de User y UserPerfil.
