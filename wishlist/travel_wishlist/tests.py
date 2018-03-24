from django.test import TestCase
from django.urls import reverse
from .forms import VisitPlaceForm

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

    # test visited places
    def test_view_places_visited(self):
        response = self.client.get(reverse('places_visited'))
        # check if the correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')

        # data sent to the template
        data_rendered = list(response.context['visited'])

        # data expected. Items with visited = False
        data_expected = list(Place.objects.filter(visited=True))

        # verify if the data sent to template and data expected are the same
        self.assertCountEqual(data_rendered, data_expected)

    # test detailed page for a place with visited=False
    def test_detailed_view_visited_false(self):
        response = self.client.get(reverse('place_detail', kwargs={'pk': 2}))
        # check if the correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/place_detail.html')

        # data sent to the template
        data_rendered = [response.context['place']]

        # data expected. Pk=2
        data_expected = Place.objects.filter(pk=2)

        # retrieve the form being displayed
        form = response.context['form']

        # verify if the data sent to template and data expected are the same
        self.assertCountEqual(data_rendered, data_expected)

        # verify that the form is a VisitPlaceForm
        self.assertIsInstance(form, VisitPlaceForm)

    # visited place will render the place information, but not VisitPlaceForm
    def test_detailed_view_visited_true(self):
        response = self.client.get(reverse('place_detail', kwargs={'pk': 3}))
        # check if the correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/place_detail.html')

        # data sent to the template
        data_rendered = [response.context['place']]

        # data expected. Pk=3
        data_expected = Place.objects.filter(pk=3)

        # verify if the data sent to template and data expected are the same
        self.assertCountEqual(data_rendered, data_expected)

        # verify that the form is not rendered if we select a visited place
        with self.assertRaises(KeyError) as context:
            form = response.context['form']
            self.assertIsInstance(form, None)