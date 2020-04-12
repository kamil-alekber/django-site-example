from django.db import models

# Create your models here.
# inherit from models.model


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    col_test = models.CharField(default="", max_length=100)
    # when removing the existing row that is filled with the info it is gonna be lost when migrating
    # can be null blank=True
    thumb = models.ImageField(default="default.png", blank=True)
    # author

    # instead of Article: object Article shows title
    # and it changed it in the admin section
    def __str__(self):
        return self.title

    # model to cut down the body of a blog

    def snippet(self):
        return self.body[:50]
