from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.TextField(max_length=100,null=True)
    phone=models.TextField(max_length=100,null=True)
    email=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.name

