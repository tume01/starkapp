from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.TextField(max_length=200)
    percentage = models.FloatField()
    status = models.IntegerField()
    #status 0 if the promotion isn't valid anymore
