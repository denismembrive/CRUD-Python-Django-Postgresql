from django.db import models   # Desde models se importara la clase tasks mediantes el cual el ORM de django creara sus respectivas tablas

# Create your models here.
# Creamos la clase Task que creara nuestara tabla
class Task(models.Model):   
    title = models.CharField(max_length=100)  # Determinamos que nuestro titulo tendra como maximo 100 caracteres
    description = models.TextField(blank=True)  # No hay restriccion de caracteres, pero al tener el blanck=True da la condicion de que clearno es necesario agregarlo
