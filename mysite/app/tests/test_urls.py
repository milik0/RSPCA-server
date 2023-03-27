from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import IndexView, AnimalView, EditAnimalView, DeleteAnimalView

class TestUrls(SimpleTestCase):
    """
    The test urls class
        * test_index_url_is_resolved: Test the index url
        * test_create_url_is_resolved: Test the create url
        * test_edit_url_is_resolved: Test the edit url
        * test_delete_url_is_resolved: Test the delete url
    """
    def test_index_url_is_resolved(self):
        """
        Test the index url
            * url: The url to test
            * resolve: The function that resolves the url
            * func.view_class: The view class that the url resolves to
            * IndexView: The view class that the url should resolve to
        """
        url = reverse('app:index')
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_create_url_is_resolved(self):
        """
        Test the create url
            * url: The url to test
            * resolve: The function that resolves the url
            * func.view_class: The view class that the url resolves to
            * AnimalView: The view class that the url should resolve to
        """
        url = reverse('app:create')
        self.assertEquals(resolve(url).func.view_class, AnimalView)

    def test_edit_url_is_resolved(self):
        """
        Test the edit url
            * url: The url to test
            * resolve: The function that resolves the url
            * func.view_class: The view class that the url resolves to
            * EditAnimalView: The view class that the url should resolve to
        """
        url = reverse('app:edit', args=[1])
        self.assertEquals(resolve(url).func.view_class, EditAnimalView)

    def test_delete_url_is_resolved(self):
        """
        Test the delete url
            * url: The url to test
            * resolve: The function that resolves the url
            * func.view_class: The view class that the url resolves to
            * DeleteAnimalView: The view class that the url should resolve to
        """
        url = reverse('app:delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, DeleteAnimalView)
