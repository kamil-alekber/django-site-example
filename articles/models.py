from django.db import models

# Create your models here.
# inherit from models.model


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add thumbnail
    # author

    # instead of Article: object Article shows title
    # and it changed it in the admin section
    def __str__(self):
        return self.title
