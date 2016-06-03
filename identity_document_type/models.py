from django.db import models

class Identity_Document_Type(models.Model):
    name = models.TextField(max_length=200)
    descripcion = models.TextField(max_length=200)
    status = models.IntegerField()