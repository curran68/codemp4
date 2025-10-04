# tests_app/tests.py

from django.test import TestCase
from bands.models import Band
from bands.views import band_list
from django.urls import reverse

# Example: Testing a Model
class BandModelTest(TestCase):
    def test_band_creation(self):
        band = Band.objects.create(
            name="Test Band", 
            genre="Rock", 
            bio="A test band bio"
        )
        self.assertEqual(band.name, "Test Band")
        self.assertEqual(str(band), "Test Band")

# Example: Testing a View's Response
class BandListViewTest(TestCase):
    def test_view_uses_correct_template(self):
        # Assumes you have a URL named 'bands:band_list'
        url = reverse('bands:band_list') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bands/bands.html')