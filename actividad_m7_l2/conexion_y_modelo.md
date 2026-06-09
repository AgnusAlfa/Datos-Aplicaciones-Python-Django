Operaciones CRUD en el ORM de Django

Crear: Se utiliza Libro.objects.create(...). Se crearon registros de prueba para validar la persistencia de datos.
Listar: Se utiliza Libro.objects.all() para obtener un QuerySet con todos los objetos de la tabla.
Buscar: Se utiliza Libro.objects.filter(titulo="...") para realizar consultas específicas.
Actualizar: Se obtiene el objeto con .get(), se modifica el atributo disponible y se persiste mediante .save().
Eliminar: Se selecciona el registro con .get() y se utiliza el método .delete() para removerlo de la base de datos.
