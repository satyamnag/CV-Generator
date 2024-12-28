from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=1000)
    address=models.TextField(max_length=1000, blank=True)
    city=models.CharField(max_length=1000)
    state=models.CharField(max_length=1000)
    pin_code=models.CharField(max_length=1000)
    contact_number=models.CharField(max_length=1000)
    email=models.EmailField()
    linkedin_id=models.CharField(max_length=1000)
    summary=models.TextField(max_length=10000, blank=True)
    skills=models.TextField(max_length=10000, blank=True)
    experience=models.TextField(max_length=10000, blank=True)
    higher_secondary=models.CharField(max_length=1000)
    degree=models.CharField(max_length=1000)
    certificates=models.TextField(max_length=1000, blank=True)
    projects=models.TextField(max_length=10000, blank=True)
