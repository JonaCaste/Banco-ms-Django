# Microservicio Django - Postgrade

## requirements.txt
En este archivo escribimos los paquetes que vamos a utilizar en nuestro proyecto

Posteriormente lo ejecutamos `pip requirements.txt` y el sistema instala los paquetes para nuestro proyecto

* para ver los paquetes instalados utilizamos `pip list`

## Entorno Virtual
Creamos un espacio en nuestro computador para correr un proyecto con requerimientos especificos

* Para crear nuestro entorno virtual utilizamos `py -m venv env`
* Ahora iniciamos nuestro entorno con el comando `env/Scripts/activate`
    * En windows ejecutamos este comando para evitar errores `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`
* instalamos nuestros paquetes cn el comando `pip install -r requirements.txt`

## Creamos un proyecto de Django
Para crear nuestro proyecto ejecutamos `django-admin startproject auth_ms .`

* La explicacion esta al principio de cada archivo

## Token DRF
Sistema de token de Django Restframework (mas simple de configurar)

* Realizamos la config en `auth_ms/settings.py`

## Apps de Django
Agregamos los modulos a `INSTALLED_APPS` en `auth_ms/settings.py`

* Tambien agregamos `SITE_ID = 1` que señala que este es el sitio principal, donde vamos a realizar la autenticación

## Ejecutar el servidor
Para ejecutar el servidor en local escribimos `py manage.py runserver`

## Migraciones
Django crea un "Archivo de instrucciones", que posteriormente se envia a la DB y se crea la DB

* `py manage.py makemigrations` -> "crear archivo de instrucciones"
* `py manage.py migrate`        -> "enviamos el archivo y creamos la DB"

## Django admin
Podemos acceder a config basicas del sitio web desde el endpoint `/admin/`

* para crear un super usuario utilizamos el comando `python manage.py createsuperuser`

## Urls
Aquí exponemos los endpoints de nuestro backned, en la dirección `auth_ms/urls.py`

## Creamos una app de Django
Para crear nuestra app ejecutamos `django-admin startapp soporte`

* agregamos al app a INSTALLED_APPS en `auth_ms/settings.py`

Explicacion al inicio de cada archivo

## Creamos los modelos
Por cada base de datos creamos su respectivo modelo en `soporte/models.py`

Posteriormente volvemos a realizar las migraciones

## Serializadores
Encargado de traducir y filtrar (establecer una comunicación) entre la vista y el modelo

creamos `serializer.py` en `soporte/`

## Vistas
Encargadas del control del CRUD - "controlador"

Por buenas practicas creamos un nuevo `urls.py` en la app `soporte/`
y posteriromente la importamos en `urls.py` del proyecto `auth_ms`

## Creamos repo
* Iniciamos un repo con `git init`
* Agregamos nuestro repo a un repo remoto con `git remote add origin https://github.com/JonaCaste/Banco-ms-django`
* Hacemos un pull para sincronizar con nuestro remoto `git pull`
* Github crea por defecto la rama main, por eso cambiamos a dicha rama con `git checkout main`
* Creamos nuestra staging area `git add .`
* Creamos nuestro commit (version) con `git commit -m ""`
* Realizamos el psuh(subir al repo remoto) con `git push origin main`
* Si no tenemos el repo(primera vez) colanmos un repo con `git clone url`

# Despliegue 
Creamos un nuevo proyecto en heroku

Instalamos el complemento de Postgresql en Heroku
* Heroku ya cuenta con docker

Agregamos las credenciales de nuestra DB a `settings.py` en `auth_ms/`
 
Y ahora:
* Eliminamos nuestra base de SQL3
* Realizamos de nuevo las migraciones
* Creamos de nuevo el super usuario

Agregamos la configuracion de heroku a nuestro proyecto Django
*   `# Heroku`
    `import django_heroku`
    `django_heroku.settings(locals())`

## Despliegue con Docker
Creamos un archivo `Dockerfile`

* En Heroku solo debemos realizar el archivo `Dockerfile`, ya que la imagen y el contenedor la realiza Heroku automaticamente.

* Recordar que podemos utilizar los comando de Docker hub

Para nuestro `Dockerfile` debemos:
* Instalar el lenguaje: en este caso Python
    * `FROM python:3`
* Python funciona con una variable de entorno para mostrar lo errores
    * `ENV PYTHONUNBUFFERED 1`
* Crear una carpeta
    * `RUN mkdir /users`
* Indicarle a Docker cual es la carpeta principal
    * `WORKDIR /users`
* Copiar el proyecto a nuestra carpeta del contenedor
    * `ADD . /users/`
* Instalar las libreria
    * `RUN pip install -r requirements.txt`
* Exponer puertos (vienen cerrados por defecto)
    * `EXPOSE 8000`
* Hacemos las migraciones y ejecutamos el servidor
    * `CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT`
    o
    * `RUN python manage.py makemigrations`
    * `RUN python manage.py migrate`
    * `python manage.py runserver 0.0.0.0:$PORT`


## Comando Docker
* `FROM ...`        -> se usa cuando queremos importar otra imagen
* `ENV ...`         -> cambiar una variable de entorno
* `mkdir /...`      -> crear una carpeta
* `RUN ...`         -> corre ese comando
* `WORKDIR ...`     -> directorio de trabajo 
* `ADD ... /.../`   -> agregar archivos al contenedor (que /donde/)
* `EXPOSE ...`      -> abrir un puerto
* `CMD ...`         -> ejecutar codigo en la terminal

## Despliegue en Heroku
Realizamos el despliegue de nuestro proyecto creada con Heroku
* `heroku login`
* Conectar Docker de nuestro sistema a Docker de Heroku (en windows, abrir el Docker Desktop)
    * `heroku container:login`
* Creamos la imagen (nombre del proyecto de heroku)
    * `heroku container:push web --app banco-ms-django`
* Ponemos a correr el contenedor (nombre del proyecto de heroku)
    * `heroku container:release web --app banco-ms-django`