"""
Models for news articles.
"""
from django.db import models


class Category(models.Model):
    """
    Category for news articles.
    """

    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.name)


class New(models.Model):
    """
    A news article.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    is_scandal = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.title)


class Image(models.Model):
    """
    An image associated with a news article.
    """

    news = models.ForeignKey(New, on_delete=models.CASCADE)
    image_url = models.URLField()

    def __str__(self) -> str:
        return f"{self.news} image"
