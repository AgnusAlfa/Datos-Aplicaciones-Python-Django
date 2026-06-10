from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    paginas = models.IntegerField()
    disponible = models.BooleanField(default=True)

    # Método para que al consultarlos veamos su título en la consola
    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    

