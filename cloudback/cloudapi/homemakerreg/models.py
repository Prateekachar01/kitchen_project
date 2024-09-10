from django.db import models

# Create your models here.
import random
import string

class HomeMakerReg(models.Model):
    userId = models.CharField(max_length=10, null=True, blank=True)
    password = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=25, null=True, blank=True)
    phoneNumber = models.CharField(max_length=25, null=True, blank=True)
    email = models.CharField(max_length=25, null=True, blank=True)
    area = models.CharField(max_length=25, null=True, blank=True)
    status= models.CharField(max_length=25, null=True, blank=True)
    def generate_random_string(self, num_digits, num_letters):
        digits = ''.join(random.sample(string.digits, k=num_digits))
        letters = ''.join(random.sample(string.ascii_uppercase, k=num_letters))
        return ''.join(random.sample(digits + letters, k=num_digits + num_letters))
    
    def save(self, *args, **kwargs):
        if not self.userId:
            self.userId = "CK" + self.generate_random_string(2, 2)
        if not self.password:
            self.password = self.generate_random_string(3, 3)

        super().save(*args, **kwargs)

    def _str_(self):
        return self.name