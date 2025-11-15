from django.test import TestCase
from django.contrib.auth.models import User

class UserTests(TestCase):
    def test_signup(self):
        response = self.client.post('/users/signup/', {
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': 'ComplexPass123',
            'password2': 'ComplexPass123'
        })
        self.assertEqual(User.objects.count(), 1)
        self.assertRedirects(response, '/')
    
    def test_login_logout(self):
        User.objects.create_user(username='user', password='pass12345')
        login = self.client.login(username='user', password='pass12345')
        self.assertTrue(login)
        response = self.client.get('/users/logout/')
        self.assertRedirects(response, '/')
