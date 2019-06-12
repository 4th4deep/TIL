from django.db import models
from django.conf import settings
# settings.AUTH_USER_MODEL

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content2 = models.TextField()
    content3 = models.TextField()
    content4 = models.TextField()
    content5 = models.TextField()
    content6 = models.TextField()
    content7 = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)