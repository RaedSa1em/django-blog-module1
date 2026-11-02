from django.contrib import admin


from blog.models.post import Post
from blog.models.category import Category
from blog.models.user import User
from blog.models.comment import Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('tittle_id', 'title', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content', 'user_name')
    ordering = ('-tittle_id',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    filter_horizontal = ('Categories',)  


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'first_name', 'last_name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user_name', 'email', 'first_name', 'last_name')
    ordering = ('-created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    list_filter = ('created_at', 'post', 'author')
    search_fields = ('content', 'author__user_name', 'post__title')
    ordering = ('-created_at',)