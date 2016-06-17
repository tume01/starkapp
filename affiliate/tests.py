from django.test import TestCase
from .forms import AffiliateForm

# Create your tests here.
class AffiliateForm(TestCase):

    def test_valid_data(self):
        form=AffiliateForm({'name':'Walter',
                            'paternalLastName':'Segama',
                            'maternalLastName': 'Segama',
                           'num_doc':77068833,
                            'phone':993904208,
                            'address':'av.universitaria',
                            'email':'correo@gmail.com'})
        self.assertTrue(form.is_valid())

    def test_empty_name(self):
        form = AffiliateForm({'name': '',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_long_name(self):
        name = ''
        for i in range(201):
            name += 'a'

        form = AffiliateForm({'name': name,
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_numeric_name(self):
        form = AffiliateForm({'name': 12345,
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_empty_paternal_lastname(self):
        form = AffiliateForm({'name': 'Walter',
                              'paternalLastName': '',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_long_paternal_lastname(self):
        name = ''
        for i in range(201):
            name += 'a'

        form = AffiliateForm({'name': 'Walter',
                              'paternalLastName': name,
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_numeric_paternal_lastname(self):
        form = AffiliateForm({'name': 'Walter',
                              'paternalLastName': 12345,
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_empty_maternal_lastname(self):
        form = AffiliateForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': '',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_long_maternal_lastname(self):
        name = ''
        for i in range(201):
            name += 'a'

        form = AffiliateForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': name,
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_numeric_maternal_lastname(self):
        form = AffiliateForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 12345,
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_non_numeric_doc(self):
        form = AffiliateForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 'abcde',
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_empty_doc(self):
        form = AffiliateForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': '',
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_non_numeric_phone(self):
        form = AffiliateForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 'abcde',
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_empty_phone(self):
        form = AffiliateForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': '',
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_empty_address(self):
        form = AffiliateForm({'name': '',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': '',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_long_address(self):
        address = ''
        for i in range(201):
            address += 'a'

        form = AffiliateForm({'name': name,
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': address,
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_numeric_address(self):
        form = AffiliateForm({'name': 12345,
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 123456,
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_empty_email(self):
        form = AffiliateForm({'name': '',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': ''})
        self.assertFalse(form.is_valid())

    def test_long_email(self):
        email = ''
        for i in range(201):
            email += 'a'

        form = AffiliateForm({'name': name,
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': email})
        self.assertFalse(form.is_valid())

    def test_numeric_email(self):
        form = AffiliateForm({'name': 12345,
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 12345})
        self.assertFalse(form.is_valid())

