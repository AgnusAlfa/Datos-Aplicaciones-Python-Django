from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    # Campo nuevo:
    isbn = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return self.titulo
    

    
