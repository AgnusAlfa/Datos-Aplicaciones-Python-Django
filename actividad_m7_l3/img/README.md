Modulo 7 - Actividad N°3
Acceso a datos en Aplicaciones Python-Django

Pasos realizados para lograr la tarea:

1. Preparación del entorno: Creación de la carpeta del proyecto y configuración de un entorno virtual (env) para aislar las dependencias. Instalación de Django y psycopg2-binary.
2. Proyecto y App: Creación del proyecto Django ("blog_project") y la aplicación ("blog"). Registro de la app en settings.py.
3. Base de Datos: Levantamiento de un contenedor Docker con PostgreSQL 16, configurando la base de datos "blog_db", el usuario "admin_blog" y su contraseña.
4. Conexión: Configuración del diccionario DATABASES en settings.py para conectar Django con PostgreSQL y ejecución de las migraciones iniciales.
5. Modelado de Datos: Creación de los modelos Autor y Articulo en models.py, estableciendo una relación de llave foránea (ForeignKey) de uno a muchos.
6. Migraciones: Ejecución de makemigrations y migrate para traducir los modelos de Python a tablas relacionales en Postgres.
7. Consultas ORM: Uso de "python manage.py shell" para realizar operaciones de creación (create) y lectura/filtrado (all, filter) sobre los modelos creados. (Ver capturas adjuntas).