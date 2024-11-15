from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.SmallIntegerField(null=True)
    pass

class Vakansi(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media/v_photos',null=True,blank=True)
    title = models.CharField(max_length=50,null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__ (self):
        return f"{self.title} by: {self.user.username}"

class Request(models.Model):
    vakansi = models.ForeignKey(Vakansi,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__ (self):
        return f"{self.vakansi.title} requested by {self.user.username}"
