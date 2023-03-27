# Test the models
#
# Path: mysite\app\tests\test_models.py
from django.test import TestCase
from ..models import Animal, Species

class TestModels(TestCase):

        def setUp(self):
            self.species = Species.objects.create(name='Dog')
            self.species.save()
            self.animal = Animal.objects.create(species=self.species, name='Doggo', image='img_data/doggo.jpg')
            self.animal.save()

        def test_animal_str(self):
            self.assertEquals(str(self.animal), 'Doggo')

        def test_species_str(self):
            self.assertEquals(str(self.species), 'Dog')

        def test_animal_was_published_recently_with_future_animal(self):
            """
            was_published_recently() returns False for animals whose pub_date
            is in the future.
            """
            time = timezone.now() + datetime.timedelta(days=30)
            future_animal = Animal(pub_date=time)
            self.assertIs(future_animal.was_published_recently(), False)

        def test_animal_was_published_recently_with_old_animal(self):
            """
            was_published_recently() returns False for animals whose pub_date
            is older than 1 day.
            """
            time = timezone.now() - datetime.timedelta(days=1, seconds=1)
            old_animal = Animal(pub_date=time)
            self.assertIs(old_animal.was_published_recently(), False)

        def test_animal_was_published_recently_with_recent_animal(self):
            """
            was_published_recently() returns True for animals whose pub_date
            is within the last day.
            """
            time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
            recent_animal = Animal(pub_date=time)
            self.assertIs(recent_animal.was_published_recently(), True)