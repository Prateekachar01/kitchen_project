from django.db import models

# Create your models here.

class AddOrder(models.Model):
    foodName=models.CharField(max_length=255,null=True,blank=True)
    price=models.CharField(max_length=55,null=True,blank=True)
    category=models.CharField(max_length=255,null=True,blank=True)
    userId=models.CharField(max_length=15,null=True,blank=True)
    orderDate=models.DateTimeField(auto_now_add=True)
    kitchenId=models.CharField(max_length=115,null=True,blank=True)
    status=models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self) :
        return self.foodName
    


