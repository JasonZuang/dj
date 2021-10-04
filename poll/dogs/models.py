from django.db import models

# Create your models here.
class Dogs(models.Model):
	breed = models.CharField(max_length=120)
	name = models.CharField(max_length=200)
