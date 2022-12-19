from django.db import models
import uuid

class Contactus(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=50)
    phone=models.CharField( max_length=50)
    queries=models.TextField( max_length=50)
    
    def __str__(self):
        return str(self.name)