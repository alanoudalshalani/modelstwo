from django.db import models

# Create your models here.

class Resturant(models.Model):
    name = models.CharField(max_lenght=30)
    description = models.TextField(default="")
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_time = models.DateTimeField(auto_now_add=True)