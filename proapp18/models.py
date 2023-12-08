from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer_model(User):
    phone = models.PositiveBigIntegerField()
    dob = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=10,choices=[['Male','Male'],['Female','Female']])


    