from django.contrib import admin

from .models import Feed, FeedContent, Tag


admin.site.register(Feed)
admin.site.register(FeedContent)

admin.site.register(Tag)
