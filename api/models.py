from django.db import models

# Create your models here.
class Register(models.Model):
    uid = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob =models.CharField( max_length=50)
    place_of_birth_city = models.CharField(max_length=50)
    birth_state = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    whatsapp_no = models.CharField(max_length=50)
    college_state = models.CharField(max_length=50)
    college_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    passing_year = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    permanent_address = models.CharField(max_length=50)



class Passkey(models.Model):
    uid = models.CharField( max_length=50, unique=True)
    passkey = models.CharField(max_length=4)
    active = models.BooleanField(default=True)
# Create your models here.


class JobCode(models.Model):
    jobcode = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)
    campus = models.CharField(max_length=50) 