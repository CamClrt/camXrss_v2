from django.contrib import admin

from .models import Feed, FeedContent, Tag


# TODO: take a look at https://pypi.org/project/django-reorder-admin/ to reorder models in Django admin


class FeedContentInline(admin.StackedInline):
    model = FeedContent


class FeedAdmin(admin.ModelAdmin):
    model = Feed
    inlines = [FeedContentInline]


class FeedContentAdmin(admin.ModelAdmin):
    model = FeedContent


class TagAdmin(admin.ModelAdmin):
    model = Tag


admin.site.register(Feed, FeedAdmin)
admin.site.register(FeedContent, FeedContentAdmin)
admin.site.register(Tag, TagAdmin)
