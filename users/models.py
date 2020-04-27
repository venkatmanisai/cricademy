from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    phone_1 = models.CharField(max_length=10)
    phone_2 = models.CharField(max_length=10, null=True)
    dob = models.DateField(null=True)
    institute = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=250, null=True)
    pincode = models.IntegerField(default=0, null=True)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name


