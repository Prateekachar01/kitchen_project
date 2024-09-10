from django.db import models

# Create your models here.
class CloudAdmin(models.Model):
    userId=models.CharField(max_length=10,null=True,blank=True)
    password=models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.userId
