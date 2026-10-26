from django.db import models

# Create your models here.
class Post(models.Model):
    tittle_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length=100, default='Anonymous')
    def __str__(self):
        return self.title

class User(models.Model):
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    #post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #def __str__(self):
        #return f"Comment by {self.user.user_name} on {self.post.title}"