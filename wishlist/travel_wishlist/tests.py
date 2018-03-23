from django.test import TestCase
from django.urls import reverse

from .models import Place


# Create your tests here.
class TestViewHomePageIsEmptyList(TestCase):

    # tests if it displays wishlist.html template
    def test_load_home_page_shows_empty_list(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertFalse(response.context['places']) #empty lists are false


class TestWishList(TestCase):
    # test data
    fixtures = ['test_places']

    def test_view_wishlist(self):
        response = self.client.get(reverse('place_list'))
        # check if the correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # data sent to the template
        data_rendered = list(response.context['places'])

        # data expected. Items with visited = False
        data_expected = list(Place.objects.filter(visited=False))

        # verify if the data sent to template and data expected are the same
        self.assertCountEqual(data_rendered, data_expected)

