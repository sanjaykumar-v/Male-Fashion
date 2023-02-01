from django.db import models

# Create your models here.
class Admins(models.Model):
    Name = models.CharField(max_length=30,null=True,blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Username = models.CharField(max_length=25, null=True, blank=True)
    Password = models.CharField(max_length=25, null=True, blank=True)
    Confirm = models.CharField(max_length=25, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)


class Category(models.Model):
    Name = models.CharField(max_length=25, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

class Productss(models.Model):
    Name = models.CharField(max_length=25, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Brand = models.CharField(max_length=25, null=True, blank=True)
    Description = models.CharField(max_length=250, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Categry = models.CharField(max_length=20, null=True, blank=True)

class contacts(models.Model):
    Name = models.CharField(max_length=25, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    message = models.CharField(max_length=250, null=True, blank=True)


