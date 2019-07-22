from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    submitted_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    submitted_at = models.DateTimeField(auto_now=True)
