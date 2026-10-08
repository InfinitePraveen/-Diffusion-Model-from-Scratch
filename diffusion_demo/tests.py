from django.test import SimpleTestCase
class HomePageTests(SimpleTestCase):
    def test_home_page(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Diffusion Model from Scratch')
