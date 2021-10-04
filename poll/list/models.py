from django.db import models

# Create your models here.
class list(models.Model):
	title = models.CharField(max_length=120) #
	items = models.JSONField()
	summary = models.TextField(default = 'This list is for', blank = True, null = True)
