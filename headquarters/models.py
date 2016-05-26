from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Hearquarters(object):
	name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
	