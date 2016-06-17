from django.test import TestCase
from .forms import GuestForm

# Create your tests here.
class GuestFormTest(TestCase):

    def test_valid_data(self):
        form= GuestForm({'name':'Walter',
                         'surname':'Segama',
                         'dni':77068833,
                        })
        self.assertTrue(form.is_valid())

    def test_empty_name(self):
        form = GuestForm({'name': '',
                          'surname': 'Segama',
                          'dni': 77068833,
                          })
        self.assertFalse(form.is_valid())

    def test_long_name(self):
        name = ''
        for i in range(201):
            name+='a'

        form = GuestForm({'name': name,
                          'surname': 'Segama',
                          'dni': 77068833,
                          })

        self.assertFalse(form.is_valid())

    def test_empty_surname(self):
        form = GuestForm({'name': 'Walter',
                          'surname': '',
                          'dni': 77068833,
                          })
        self.assertFalse(form.is_valid())

    def test_long_surname(self):
        surname = ''
        for i in range(201):
            surname += 'a'

        form = GuestForm({'name': 'Walter',
                          'surname': surname,
                          'dni': 77068833,
                          })

        self.assertFalse(form.is_valid())

    def test_non_numeric_dni(self):
        form = GuestForm({'name': 'Walter',
                          'surname': 'Segama',
                          'dni': 'abc',
                          })
        self.assertFalse(form.is_valid())

    def test_negative_dni(self):
        form = GuestForm({'name': 'Walter',
                          'surname': 'Segama',
                          'dni': -1,
                          })
        self.assertFalse(form.is_valid())

    def test_empty_dni(self):
        form = GuestForm({'name': 'Walter',
                          'surname': 'Segama',
                          'dni': '',
                          })
        self.assertFalse(form.is_valid())

