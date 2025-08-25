from django.contrib import admin
from posts.models import Post, PostImage, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "content",
    ]

    inlines = [
        CommentInline,
    ]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo",
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
    ]