Modulo 7 - Actividad N° 5: Consultas Personalizadas

1. ¿Qué ventajas encuentras en usar el ORM frente a SQL tradicional?
La principal ventaja es la **abstracción y la seguridad**. El ORM permite escribir consultas utilizando sintaxis de Python, lo que hace que el código sea más legible y mantenible. Además, previene automáticamente ataques de inyección SQL. Otra gran ventaja es que el código es agnóstico a la base de datos; es decir, las mismas consultas en Python funcionarán igual si el día de mañana decidimos cambiar de PostgreSQL a MySQL o SQLite, sin tener que reescribir sentencias SQL específicas.

2. ¿En qué situaciones te parece útil ejecutar SQL directamente desde Django?
Ejecutar SQL en crudo (usando `raw()` o `connection.cursor()`) es útil en escenarios muy específicos de **optimización extrema o complejidad**. Por ejemplo:
* Cuando necesitamos ejecutar reportes matemáticos muy complejos con múltiples agrupaciones (JOINs masivos) que el ORM de Django traduciría de forma ineficiente.
* Cuando queremos aprovechar funciones específicas del motor de base de datos (por ejemplo, funciones exclusivas de PostgreSQL que el ORM no soporta de forma nativa).
* Cuando estamos migrando un sistema antiguo y ya tenemos *queries* de SQL puro creadas y testeadas por un Administrador de Base de Datos (DBA).

3. ¿Qué dificultades encontraste al trabajar con consultas más avanzadas?
Al trabajar con consultas avanzadas, la principal curva de aprendizaje es entender la sintaxis específica que utiliza Django para reemplazar a SQL. Por ejemplo, memorizar el uso de los "lookups" con doble guion bajo (como `__gt` para mayor que, o `__lt` para menor que) en lugar de los clásicos operadores matemáticos `>`, `<`. Además, al usar `connection.cursor()`, los resultados se devuelven como tuplas puras de Python en lugar de objetos instanciados, lo que nos obliga a mapear manualmente los datos mediante sus índices (ej. `fila[0]`, `fila[1]`) para poder imprimirlos correctamente.