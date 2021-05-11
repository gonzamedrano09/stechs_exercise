# StechsExercise

### Pasos para la ejecución del proyecto

1. Teniendo instalado Python 3.6 y virtualenv, crear el entorno virtual con `python3 -m virtualenv venv`.
2. Activar el entorno virtual, en Linux lo hacemos con `source venv/bin/activate`.
3. Instalar los paquetes necesarios en el entorno virtual con `pip install -r requirements.txt`.
4. Crear una base de datos MySQL con el nombre "stechs".
5. Crear la tabla `docsis_update` y agregar algunos registros con el archivo .sql de nombre "modems.sql".   
6. Agregar un usuario y password para poder acceder a la base de datos MySQL en el archivo "my.cnf".
7. Ejecutar las migraciones necesarias con `python manage.py migrate`.
8. Correr el servidor para pruebas de django con `python manage.py runserver`.
9. Acceder a la interfaz web a través de [http://localhost:8000/][url]

[url]: http://localhost:8000/

### Requerimientos futuros a tener en cuenta en el modelado

1. Para soportar alias de los cablemodems, podría agregarse por cada modelo del archivo JSON un campo de clave "alias" 
   que contenga una lista de strings, los cuales deberán ser tenidos en cuenta al hacer la consulta a la base de datos.
2. Para agregar la versión de software de los modelos basta con agregar el campo de clave "swver" y agregarlo en cada 
   registro en el momento de agregar un modelo al archivo JSON, para los que ya están agregados, se podría realizar un
   script que consulte los cable modems con modelos ya agregados para obtener su versión de y guardalo.
3. Para obtener métricas sobre los cable modems por modelo y por fabricante lo mejor me parecería agregar un endopoint
   distinto exclusivamente para esto, en donde se trabaje con el archivo json parseado a un diccionario de Python, de 
   esta forma hasta podría realizarse una interfaz aparte a modo de reporte para acceder a estos datos.