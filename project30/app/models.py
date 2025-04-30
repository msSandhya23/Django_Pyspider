from django.db import models
from app.models import *
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.
 
class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('Email is not provided')
        nemail = self.normalize_email(email)
        user = self.model(email=nemail,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,first_name,last_name,password):
        user = self.create_user(email,first_name,last_name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    def __str__(self):
        return self.email

