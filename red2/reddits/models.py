import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Subreddit(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def current_count(self):
        return len(self.post_set.all())

    def today_count(self):
        day = timezone.now() - datetime.timedelta(hours=24)
        return len(Subreddit.objects.filter(date_added_get=day))

    def daily_avreage(self):
        week = timezone.now() - datetime.timedelta(days=7)


        return


class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(default="empty")
    url = models.URLField(null=True)
    slug = models.SlugField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    subreddit = models.ForeignKey(Subreddit)
    user = models.ForeignKey(User)
    def is_recent(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.posted_at
    def is_hot(self):
       if self.comments_set.all()



class Comment(models.Model):
    comment_text = models.TextField(default="empty")
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} posted by {} on {}" .format(self.id, self.user, self.date_added)