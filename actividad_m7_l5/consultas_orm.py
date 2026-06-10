import os
import django

# 1. Configuración necesaria para usar el ORM fuera del entorno web
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_consultas.settings')
django.setup()

from django.db import connection
from django.db.models import Count
from biblioteca.models import Libro

print("\n--- 1. RECUPERACIÓN DE REGISTROS ---")

# a) Recupera todos los libros registrados.
# objects.all() devuelve todos los registros de la tabla sin filtros.
todos_los_libros = Libro.objects.all()
print("\nTodos los libros:")
for libro in todos_los_libros:
    print(f"- {libro.titulo} ({libro.paginas} págs)")

# b) Recupera solo los libros cuyo autor sea "Gabriel García Márquez".
# objects.filter() busca coincidencias exactas en la columna 'autor'.
libros_gabo = Libro.objects.filter(autor="Gabriel García Márquez")
print("\nLibros de Gabriel García Márquez:")
for libro in libros_gabo:
    print(f"- {libro.titulo}")

# c) Recupera los libros que tienen más de 200 páginas.
# El sufijo '__gt' significa "greater than" (mayor que) en el ORM.
libros_largos = Libro.objects.filter(paginas__gt=200)
print("\nLibros con más de 200 páginas:")
for libro in libros_largos:
    print(f"- {libro.titulo} ({libro.paginas} págs)")


print("\n--- 2. FILTROS Y EXCLUSIONES ---")

# a) Aplica un filtro para mostrar solo libros disponibles.
# objects.filter(campo=True) trae solo los registros booleanos afirmativos.
libros_disponibles = Libro.objects.filter(disponible=True)
print("\nLibros Disponibles:")
for libro in libros_disponibles:
    print(f"- {libro.titulo}")

# b) Excluye todos los libros que tengan menos de 100 páginas.
# objects.exclude() hace lo inverso al filter. El sufijo '__lt' es "less than" (menor que).
libros_no_cortos = Libro.objects.exclude(paginas__lt=100)
print("\nLibros que NO tienen menos de 100 páginas:")
for libro in libros_no_cortos:
    print(f"- {libro.titulo} ({libro.paginas} págs)")

print("\n")

print("\n--- 3. CONSULTAS PERSONALIZADAS CON SQL ---")

# a) Ejecuta una consulta SQL directa utilizando raw() ordenando por titulo.
# raw() mapea el resultado de SQL puro a objetos del modelo Libro. 
# Nota: Django nombra las tablas uniendo el nombre de la app y el modelo (biblioteca_libro).
libros_raw = Libro.objects.raw('SELECT * FROM biblioteca_libro ORDER BY titulo;')
print("\nLibros ordenados por título usando raw():")
for libro in libros_raw:
    print(f"- {libro.titulo}")

# b) Usa connection.cursor() para una query personalizada (conteo de libros por autor).
# cursor() permite ejecutar SQL puro sin pasar por los modelos, directo a la base de datos.
print("\nConteo de libros por autor usando connection.cursor():")
with connection.cursor() as cursor:
    cursor.execute("SELECT autor, COUNT(*) FROM biblioteca_libro GROUP BY autor;")
    resultados = cursor.fetchall() # Obtiene una lista de tuplas
    for fila in resultados:
        print(f"- Autor: {fila[0]} | Total: {fila[1]} libro(s)")

print("\n--- 4. CAMPOS ESPECÍFICOS Y ANOTACIONES ---")

# a) Recupera solo los títulos de todos los libros (usando values()).
# values() devuelve diccionarios en lugar de objetos completos, ahorrando memoria.
titulos = Libro.objects.values('titulo')
print("\nSolo los títulos de los libros:")
for item in titulos:
    print(f"- {item['titulo']}")

# b) Agrega una anotación (usando annotate) para contar cuántos libros hay por autor.
# Es la forma de hacer un "GROUP BY" y "COUNT" usando el poder del ORM de Django.
conteo_orm = Libro.objects.values('autor').annotate(total_libros=Count('id'))
print("\nConteo de libros por autor usando annotate() (ORM):")
for item in conteo_orm:
    print(f"- Autor: {item['autor']} | Total: {item['total_libros']} libro(s)")

print("\n=== FIN DE LAS CONSULTAS ===\n")

