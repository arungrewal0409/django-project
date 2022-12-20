# from msilib.schema import Class
from django.db import models
from datetime import datetime

class checkout (models.Model):
 first_name = models.CharField(max_length=100)
 last_name = models.CharField(max_length=130)
 Username = models.CharField(max_length=130)
 Email = models.CharField(max_length=130)
 Address = models.CharField(max_length=130)
 Address2 = models.CharField(max_length=130)
 Name_on_card = models.CharField(max_length=130)
 Credit_card_number = models.CharField(max_length=130)
 Expiration = models.CharField(max_length=130)
 CVV = models.CharField(max_length=3)

# Create your models here.
