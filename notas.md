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

## Creamos repo
* Iniciamos un repo con `git init`
* Agregamos nuestro repo a un repo remoto con `git remote add origin https://github.com/JonaCaste/Banco-ms-django`
* Hacemos un pull para sincronizar con nuestro remoto `git pull`
* Creamos nuestra staging area `git add .`
* Creamos nuestro commit (version) con `git commit -m ""`
* Realizamos el psuh(subir al repo remoto) con `git push remoto main`
* Si no tenemos el repo(primera vez) colanmos un repo con `git clone url`