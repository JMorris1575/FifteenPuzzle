from django.test import TestCase
from django.contrib.auth.models import User

class LoginTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        charlie = User.objects.create_user("Charles", password="charliespassword")

    def test_redirects_base_url_to_user_login(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/user/login/')

    def test_user_login_uses_correct_template(self):
        response = self.client.get('/user/login/')
        self.assertTemplateUsed(response, 'user/login.html')

    def test_user_login_uses_base_html(self):
        response = self.client.get('/user/login/')
        self.assertTemplateUsed(response, 'user/login.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_login_from_credentials(self):
        self.assertTrue(self.client.login(username='Charles', password='charliespassword'))
        self.assertFalse(self.client.login(username='Charles', password='nothing'))

    def test_correct_user_login_post_redirects(self):
        response = self.client.post('/user/login/', {'username': "Charles", 'password': "charliespassword"},
                                    follow=True)
        self.assertRedirects(response, '/fifteen/entry/')
        self.assertTemplateUsed(response, 'fifteen/entry.html')

    def test_bad_login_returns_to_login_with_errors(self):
        response = self.client.post('/user/login/', {'username': 'Charles', 'password': 'wrong'})
        self.assertEqual(response.request['PATH_INFO'], '/user/login/')
        self.assertContains(response, 'Please enter a correct username and password.')




