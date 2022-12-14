from django.db import models

# Create your models here.
"""
class Post:
    title: str
    author: str
    content: str
    thumbnail: image
"""


class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    content = models.TextField()
    thumbnail = models.ImageField(
        upload_to="thumbnails/", default="deafault.png")

    def __str__(self):
        post = {
            "title": self.title,
            "author": self.author,
        }
        return f"{post}"
