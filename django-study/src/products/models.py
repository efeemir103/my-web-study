from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    descripton = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='this is so cool! :D')