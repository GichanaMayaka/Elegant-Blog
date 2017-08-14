from django.contrib.syndication.views import Feed
from .models import Entry


class LatestPosts(Feed):
    title = 'Cask of the Red Death'
    link = '/feed/'
    description = 'Latest Posts'

    @staticmethod
    def items():
        return Entry.objects.published()[:5]