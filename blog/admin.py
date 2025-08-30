from django.contrib import admin
from .models import Author, Post, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "published_recently")
    inlines = [CommentInline]

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)