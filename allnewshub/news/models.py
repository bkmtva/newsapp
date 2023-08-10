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
    large_image_url = models.URLField(null=True)
    small_image_url = models.URLField(null=True)

    def __str__(self) -> str:
        return str(self.title)
