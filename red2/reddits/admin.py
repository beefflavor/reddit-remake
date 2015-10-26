from django.contrib import admin
from reddits.models import Subreddit, Post, Comment

@admin.register(Subreddit)
class SubredditAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date_added']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'url', 'slug', 'date_added', 'user']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_text', 'post', 'user', 'date_added']

