from django.db import models
from model_utils.models import TimeStampedModel

from . import Tag


# https://fr.wikipedia.org/wiki/RSS

class Feed(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(unique=True, blank=False)
    last_build_date = models.DateTimeField()
    language = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, related_name="feed_tags", related_query_name="feed_tags")

    def __str__(self) -> str:
        return f"{self.title}: {self.url}"


class FeedContent(TimeStampedModel):

    CONTENT_TYPE = [
        ('podcast', 'Podcast'),
        ('article', 'Article'),
        ('youtube', 'Youtube'),
        ('newsletter', 'Newsletter'),
    ]

    guid = models.CharField(max_length=50, unique=True, blank=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    content_type = models.CharField(max_length=25, choices=CONTENT_TYPE, default="article")
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="content_tags", related_query_name="content_tags")

    def __str__(self) -> str:
        return f"{self.guid}/{self.content_type}: {self.title}"
