Modulo 7 - Actividad N° 4
Gestión de Migraciones en Django

1. Comprensión teórica

**¿Qué es una migración en Django?**
Una migración es la forma en que Django propaga y aplica los cambios que hacemos en nuestros modelos (código Python) al esquema de la base de datos relacional. Funciona como un sistema de control de versiones para la estructura de la base de datos.

**¿Qué problema soluciona respecto a los cambios en los modelos?**
Soluciona el problema de tener que escribir sentencias SQL manuales (como `ALTER TABLE`) cada vez que la estructura de los datos evoluciona. Además, permite mantener un historial cronológico de los cambios, lo que facilita el trabajo en equipo y evita la pérdida accidental de datos al modificar tablas existentes.

**¿Por qué no basta con modificar el archivo models.py directamente sin hacer migraciones?**
Porque la base de datos (SQLite, PostgreSQL, etc.) no entiende código Python. Al modificar `models.py`, solo actualizamos la representación de los datos en nuestro backend. Es obligatorio ejecutar el proceso de migraciones para que Django traduzca ese código Python a lenguaje SQL y ejecute los cambios físicamente en el motor de la base de datos.


2. Crear y aplicar migraciones

**Comandos ejecutados y su función:**

* `python manage.py makemigrations`: Este comando analiza el archivo `models.py` en busca de cambios (creación de modelos, nuevos campos, etc.). Si encuentra modificaciones, genera un nuevo archivo de migración (un "plano" con las instrucciones en código) dentro de la carpeta `migrations` de la aplicación.
* `python manage.py migrate`: Este comando toma los archivos de migración pendientes que generó el paso anterior, los traduce a sentencias SQL, y las ejecuta directamente en el motor de la base de datos para alterar físicamente las tablas (en este caso, agregando la columna `isbn`).


3. Aplicar migraciones existentes (Experimentación)

**¿Qué sucedió al eliminar la migración y volver a ejecutar los comandos?**
Al eliminar el archivo físico de la migración (`0002_...`) y ejecutar `makemigrations`, Django detectó el campo `isbn` en `models.py` como si fuera nuevo y creó un nuevo archivo de migración. Sin embargo, al ejecutar `migrate`, la terminal arrojó "No migrations to apply". Esto ocurre porque Django guarda un historial interno en la base de datos (en la tabla `django_migrations`). Al ver que una migración "0002" ya estaba registrada como aplicada previamente, ignoró el nuevo archivo para proteger la base de datos. Esto demuestra que desincronizar los archivos físicos del historial de la base de datos genera inconsistencias en el proyecto.

**¿Qué sucede si no aplicas una migración pendiente?**
Si modificamos el código en `models.py` (por ejemplo, agregamos una columna nueva), ejecutamos `makemigrations`, pero **NO** aplicamos el `migrate`, nuestro código Python y la base de datos quedan desincronizados. Cuando la aplicación intente guardar o consultar un dato usando ese nuevo campo, la base de datos arrojará un error crítico informando que dicha columna no existe, lo que provocará la caída de la aplicación.

4. Revisión de estado (Opcional)

**Comando ejecutado:** `python manage.py showmigrations`

**¿Qué información entrega y cómo saber qué migraciones ya se aplicaron?**
Este comando imprime en la terminal una lista de todas las aplicaciones del proyecto junto con sus respectivos archivos de migración. Nos permite auditar el estado actual del historial interno de Django. Para saber qué migraciones ya fueron ejecutadas y aplicadas físicamente, debemos fijarnos en los corchetes: las aplicadas tienen una equis `[X]`, mientras que las migraciones pendientes por aplicar aparecen con el espacio en blanco `[ ]`.