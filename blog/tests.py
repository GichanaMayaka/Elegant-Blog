from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Entry

# Create your tests here.


class BlogPostTest(TestCase):
    def test_create_unpublished(self):
        entry = Entry(title='Title Me', body=' ', publish=False)
        entry.save()

        self.assertEquals(Entry.objects.all().count(), 1)
        self.assertEquals(Entry.objects.published().count(), 0)

        entry.publish = True
        entry.save()

        self.assertEquals(Entry.objects.published().count(), 1)


class BlogViewTests(TestCase):
    def test_feed_url(self):
        response = self.client.get('/blog/feed/')
        self.assertIn("xml", response['Content-Type'])