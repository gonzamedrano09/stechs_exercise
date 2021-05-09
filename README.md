# StechsExercise

Pasos para la ejecución del proyecto

1. Teniendo instalado Python 3.6 y virtualenv, crear el entorno virtual con `python3 -m virtualenv venv`
2. Activar el entorno virtual, en Linux lo hacemos con `source venv/binc/activate`
3. Instalar los paquetes necesarios en el entorno virtual con `pip install -r requirements.txt`
4. Crear una base de datos MySql con el nombre "stechs"
5. Crear la tabla `docsis_update` con el archivo .sql de nombre "modems.sql"   
6. Agregar un usuario y password para poder acceder a la base de datos en el archivo "my.cnf"
7. Ejecutar las migraciones necesarias de django con `python manage.py migrate`
8. Correr el servidor de pruebas de django con `python manage.py runserver`
9. Ya puede accederse a la interfaz web a través de [http://localhost:8000/][url]

[url]: http://localhost:8000/