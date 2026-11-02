from django.db import models


class Post(models.Model):
    tittle_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name='posts')
    
    def __str__(self):
        return self.title