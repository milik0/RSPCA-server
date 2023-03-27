# Test forms

from django.test import TestCase
from ..forms import AnimalForm

class TestForms(TestCase):
    """
    The test forms class
        * test_animal_form_valid_data: Test the animal form with valid data
        * test_animal_form_no_data: Test the animal form with no data
    """
    def test_animal_form_valid_data(self):
        """
        Test the animal form with valid data
        """
        form = AnimalForm(data={
            'name': 'Doggo',
            'species': 'Dog',
            'description': 'A doggo',
            'image': 'img_data/doggo.jpg',
        })
        self.assertTrue(form.is_valid())

    def test_animal_form_no_data(self):
        """
        Test the animal form with no data
        """
        form = AnimalForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)
