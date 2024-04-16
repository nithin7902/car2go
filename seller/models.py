from django.db import models

# Create your models here.
class SellerRegistration(models.Model):
    fullname=models.TextField(max_length=100,null=True)
    email=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)

    def __str__(self):
      return self.fullname
    

class Products(models.Model):
   car_name=models.TextField(max_length=100,null=True)
   car_brand=models.TextField(max_length=100,null=True)
   car_color=models.TextField(max_length=100,null=True)
   rent_charge=models.TextField(max_length=100,null=True)
   image=models.ImageField(upload_to='images',null=True)
   topspeed=models.TextField(max_length=100,null=True)
   capacity=models.TextField(max_length=100,null=True)
   fuels=models.TextField(max_length=100,null=True)



