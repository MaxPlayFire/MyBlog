from django.contrib import admin
from .models import Author, Post, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ("created_date",)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "is_recent")
    list_filter = ("author", "published_date")
    search_fields = ("title", "content")
    inlines = [CommentInline]

    @admin.display(boolean=True, ordering="published_date", description="≤ 7 днів")
    def is_recent(self, obj):
        return obj.published_recently()

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author_name", "post", "created_date")
    list_filter = ("created_date", "post")