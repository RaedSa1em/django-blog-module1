from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_name