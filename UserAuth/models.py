from django.db import models
from rest_framework import authentication
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import stripe

"""
User Auth Models
"""

class BearerAuthentication(authentication.TokenAuthentication):
    '''
    Simple token based authentication using utvsapitoken.

    Clients should authenticate by passing the token key in the 'Authorization'
    HTTP header, prepended with the string 'Bearer '.  For example:

    Authorization: Bearer 956e252a-513c-48c5-92dd-bfddc364e812
    '''
    keyword = 'Bearer'

class UserManager(BaseUserManager):
    """ Manager for users """
    def create_user(self, email, password=None, **extra_fields):
        """ Create, save and return a new user """
        if not email:
            raise ValueError("User must have an email address")
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """ Create and return a new superuser """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class User(AbstractBaseUser, PermissionsMixin):
    """ User in the System """
    email = models.EmailField(max_length=266, unique=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
