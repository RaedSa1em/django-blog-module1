from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Categories = models.ManyToManyField('Post', related_name='posts', blank=True)
    
    def __str__(self):
        return self.name
