from django.db import models
from django.template.defaultfilters import slugify
from model_utils.models import TimeStampedModel


class Tag(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}: {self.slug}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)
