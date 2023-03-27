from django.test import TestCase, Client
from django.urls import reverse
from ..models import Animal, Species

class TestViews(TestCase):
    """
    The test views class
        * setUp: Set up the test
        * test_index_GET: Test the index GET request
        * test_create_GET: Test the create GET request
        * test_edit_GET: Test the edit GET request
        * test_delete_GET: Test the delete GET request

        * test_create_POST: Test the create POST request
        * test_edit_POST: Test the edit POST request
        * test_delete_POST: Test the delete POST request
    """
    def setUp(self):
        """
        Set up the test
            * client: The client that will be used to make requests
            * index_url: The url for the index page
            * create_url: The url for the create page
            * edit_url: The url for the edit page
            * delete_url: The url for the delete page
            * species: The species that will be used in the tests
            * animal: The animal that will be used in the tests
        """
        self.client = Client()
        self.index_url = reverse('app:index')
        self.create_url = reverse('app:create')
        self.edit_url = reverse('app:edit', args=[12])
        self.delete_url = reverse('app:delete', args=[12])
        self.species = Species.objects.create(name='Dog')
        self.species.save()
        self.animal = Animal.objects.create(species=self.species, name='Doggo', image='img_data/doggo.jpg', id=12)
        self.animal.save()

    def test_index_GET(self):
        """
        Test the index GET request
            * response: The response from the request
        """
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')

    def test_create_GET(self):
        """
        Test the create GET request
            * response: The response from the request
        """
        response = self.client.get(self.create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/detail.html')

    def test_edit_GET(self):
        """
        Test the edit GET request
            * response: The response from the request
        """
        response = self.client.get(self.edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/edit.html')

    def test_delete_GET(self):
        """
        Test the delete GET request
            * response: The response from the request
        """
        response = self.client.get(self.delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/delete.html')

    def test_create_POST(self):
        """
        Test the create POST request
            * response: The response from the request
        """
        response = self.client.post(self.create_url, {
            'species': self.species.id,
            'name': 'Doggo',
            'image': 'img_data/doggo.jpg',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '../')

    def test_edit_POST(self):
        """
        Test the edit POST request
            * response: The response from the request
        """
        response = self.client.post(self.edit_url, {
            'species': self.species.id,
            'name': 'Doggo',
            'image': 'img_data/doggo.jpg',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '../')

    def test_delete_POST(self):
        """
        Test the delete POST request
            * response: The response from the request
        """
        response = self.client.post(self.delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '../')
