1. Bases de datos en Django

- ¿Qué función cumple una base de datos dentro de una aplicación Django?
Cumple la función de almacenar, organizar y gestionar toda la información persistente de la aplicación. Básicamente, es el lugar donde se guardan los datos dinámicos (como cuentas de usuarios, productos, configuraciones, etc.) para que Django pueda consultarlos, actualizarlos o eliminarlos según las acciones que realice el usuario en el frontend.

- ¿Qué sistemas de bases de datos relacionales soporta Django por defecto?
De manera nativa (sin instalar paquetes de terceros), Django soporta oficialmente PostgreSQL, MySQL, MariaDB, Oracle y SQLite.

- ¿Cuál es el motor de base de datos que se utiliza por defecto al crear un nuevo proyecto? ¿Por qué crees que es ese?
El motor que viene configurado por defecto es SQLite (en el archivo settings.py aparece como sqlite3). Se utiliza este principalmente por su simplicidad, viene integrado directamente en Python, es un archivo local y no requiere instalar ni configurar un servidor de base de datos externo. Esto es ideal para que podamos levantar el entorno de desarrollo y empezar a programar de inmediato sin trabas de configuración.

2. ORM en Django

- ¿Qué es un ORM y cómo se diferencia de escribir sentencias SQL manualmente?

Un ORM (Mapeo Objeto-Relacional, por sus siglas en inglés) es una herramienta que nos permite interactuar con la base de datos utilizando el paradigma orientado a objetos de Python, en lugar de escribir código SQL de forma directa. La gran diferencia está en la forma de trabajar: al usar SQL manualmente, debes redactar las instrucciones exactas y preocuparte de la sintaxis específica del motor de base de datos (ej. SELECT * FROM usuarios WHERE id = 1). En cambio, con el ORM, escribes código Python estándar (ej. Usuario.objects.get(id=1)), y el propio framework se encarga de "traducir" automáticamente ese código a la sentencia SQL correcta en segundo plano.

- Menciona al menos dos ventajas de usar el ORM de Django.

1.Portabilidad: Puedes cambiar fácilmente de motor (por ejemplo, pasar del SQLite que usamos para pruebas a un PostgreSQL para producción) modificando solo la configuración. No necesitas reescribir tus consultas, el ORM adapta el SQL por ti.

2.Seguridad por defecto: El ORM de Django limpia y "escapa" automáticamente los parámetros de las consultas. Esto previene de forma nativa los ataques de inyección SQL, que son un riesgo grave cuando se construyen consultas SQL manuales concatenando textos.

- Explica qué significa que una clase modelo en Python represente una tabla en la base de datos.
Significa que Django mapea directamente la estructura de tu código con la estructura de la base de datos. En la práctica funciona así:

a.La clase que defines en Python (class Usuario(models.Model):) equivale a la tabla en la base de datos.
b.Los atributos o variables que pones dentro de esa clase (ej. nombre = models.CharField(...)) se convierten en las columnas de esa tabla.
c.Cada vez que creas un objeto o instancia nueva a partir de esa clase en tu código, estás creando una nueva fila (o registro) dentro de esa tabla.

3. Migraciones

- ¿Qué son las migraciones en Django y por qué son importantes?
Las migraciones son el mecanismo que tiene Django para propagar los cambios que hacemos en nuestros modelos (código Python) hacia el esquema de la base de datos (tablas, columnas, etc.). Piensa en ellas como un sistema de "control de versiones" para tu base de datos. Son sumamente importantes porque permiten que la estructura de la base de datos evolucione a la par con nuestro código de forma automática y segura. Esto evita que tengamos que escribir y ejecutar scripts SQL manualmente cada vez que agregamos o modificamos un campo, manteniendo la consistencia del proyecto, especialmente cuando se trabaja en equipo.

- ¿Qué comandos se utilizan para crear y aplicar migraciones?

a.Para crear una nueva migración a partir de cambios en los modelos: Se utiliza el comando python manage.py makemigrations. Al ejecutarlo, Django escanea nuestros modelos, detecta los cambios nuevos y genera un archivo de migración con las instrucciones necesarias.

b.Para aplicar las migraciones a la base de datos: Se utiliza el comando python manage.py migrate. Este comando toma los archivos de migración pendientes y los traduce a sentencias SQL que se ejecutan directamente en el motor de la base de datos, actualizando su estructura final.

4. Consultas básicas con el ORM

Para realizar estas operaciones, siempre partimos llamando al modelo Libro seguido de .objects, que es el "gestor" que Django nos da para manejar los datos.

a) Obtener todos los libros:
Para traer todo lo que haya en la tabla, usamos el método .all(): 
- libros = Libro.objects.all()

b) Filtrar los libros por autor igual a "Cervantes":
Aquí usamos el método .filter(). Es súper intuitivo porque le pasas el campo y el valor que buscas: 
- libros_cervantes = Libro.objects.filter(autor="Cervantes")

c) Obtener un libro específico por su id:
Cuando queremos buscar un registro único por su identificador (que es la clave primaria), usamos .get(). Es ideal porque nos devuelve exactamente un objeto: 
- libro_especifico = Libro.objects.get(id=1)




