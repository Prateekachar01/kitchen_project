from django.db import models

# Create your models here.
class AddFood(models.Model):

    foodName=models.CharField(max_length=255,null=True,blank=True)
    orderFrom=models.CharField(max_length=55,null=True,blank=True)
    orderTill=models.CharField(max_length=55,null=True,blank=True)
    price=models.CharField(max_length=55,null=True,blank=True)
    category=models.CharField(max_length=255,null=True,blank=True)
    userId=models.CharField(max_length=15,null=True,blank=True)
    foodFile=models.TextField(null=True,blank=True)

    def __str__(self) :
        return self.foodName