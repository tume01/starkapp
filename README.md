# starkapp

Para poder separar Bungalow y BungalowType todo se cayo
porque y estaba creado en la misma carpeta o no se.

En caso no puedan correr las migraciones aqui les dejo el workaround:

    Ir a mysql y dropear la db (DROP DATABASE database_name)
    Crearla otra vez (CREATE DATABASE database_name)

    Ya luego en la carpeta del proyecto correr otra ves
    python manage.py migrate

    y luego corren los seeders

Lamento los inconvenientes.
Alvaro Santa Cruz (01 Junio 2016)