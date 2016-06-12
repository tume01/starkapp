from django.test import TestCase
from .forms import UserForm

class UserFormTest(TestCase):

    
    def test_valid_data(self):
        form = UserForm({
            'name' : 'Enrique',
            'password' : 'a12345',
            'user_type': 1,
            })
        self.assertTrue(form.is_valid())

    def test_empty_name(self):
        form = UserForm({
            'name' : '',
            'password' : 'a12345',
            'user_type': 1,
            })
        self.assertFalse(form.is_valid())

    def test_long_name(self):
        name = ''
        for i in range(201):
            name += 'a'
            
        form = UserForm({
            'name' : name,
            'password' : 'a12345',
            'user_type': 1,
            })
        self.assertFalse(form.is_valid())


    def test_empty_password(self):
        form = UserForm({
            'name' : 'Enrique',
            'password' : '',
            'user_type': 1,
            })
        self.assertFalse(form.is_valid())

    def test_long_password(self):
        password = ''
        for i in range(201):
            password += 'a'
            
        form = UserForm({
            'name' : 'Enrique',
            'password' : password,
            'user_type': 1,
            })
        self.assertFalse(form.is_valid())

    def test_empty_user_type(self):
        form = UserForm({
            'name' : 'Enrique',
            'password' : 'a12345',
            'user_type': '',
            })
        self.assertFalse(form.is_valid())
