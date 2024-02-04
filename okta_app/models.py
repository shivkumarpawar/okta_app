from django.db import models

class Email(models.Model):
    address = models.EmailField(unique=True)

# Create your models here.
