from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return self.email
    
class Algorithm(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self): 
        return self.name
