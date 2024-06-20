from django.db import models
from datetime import date

# Create your models here.
class Libros(models.Model):
    titulo = models.CharField(max_length=60)
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateField(default=date.today)
    isbn = models.CharField(max_length=10)
    ruta_img = models.TextField(default='')

