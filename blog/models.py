from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts", null=True, blank=True)

    def __str__(self):
        return self.title
    
    def published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=7)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author_name} on {self.post.title}"