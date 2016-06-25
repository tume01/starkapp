from django.test import TestCase
from .forms import GuestForm

# Create your tests here.
class GuestFormTest(TestCase):

    def test_valid_data(self):
        form= GuestForm({'name':'Walter',
                         'paternalLastName':'Segama',
                         'document_number':77068833,
                        })
        self.assertTrue(form.is_valid())

    def test_empty_name(self):
        form = GuestForm({'name': '',
                          'paternalLastName': 'Segama',
                          'document_number': 77068833,
                          })
        self.assertFalse(form.is_valid())

    def test_long_name(self):
        name = ''
        for i in range(201):
            name+='a'

        form = GuestForm({'name': name,
                          'paternalLastName': 'Segama',
                          'document_number': 77068833,
                          })

        self.assertFalse(form.is_valid())

    def test_empty_paternalLastName(self):
        form = GuestForm({'name': 'Walter',
                          'paternalLastName': '',
                          'document_number': 77068833,
                          })
        self.assertFalse(form.is_valid())

    def test_long_paternalLastName(self):
        paternalLastName = ''
        for i in range(201):
            paternalLastName += 'a'

        form = GuestForm({'name': 'Walter',
                          'paternalLastName': paternalLastName,
                          'document_number': 77068833,
                          })

        self.assertFalse(form.is_valid())

    def test_non_numeric_document_number(self):
        form = GuestForm({'name': 'Walter',
                          'paternalLastName': 'Segama',
                          'document_number': 'abc',
                          })
        self.assertFalse(form.is_valid())

    def test_negative_document_number(self):
        form = GuestForm({'name': 'Walter',
                          'paternalLastName': 'Segama',
                          'document_number': -1,
                          })
        self.assertFalse(form.is_valid())

    def test_empty_document_number(self):
        form = GuestForm({'name': 'Walter',
                          'paternalLastName': 'Segama',
                          'document_number': '',
                          })
        self.assertFalse(form.is_valid())

