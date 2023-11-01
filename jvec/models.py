from django.db import models


class NewsItem(models.Model):
    ITEM_TYPES = (
        ('story', 'Story'),
        ('comment', 'Comment'),
        # Add more item types as needed
    )

    title = models.CharField(max_length=200)
    url = models.URLField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    item_type = models.CharField(max_length=10, choices=ITEM_TYPES)
    score = models.IntegerField()

    def __str__(self):
        return self.title
