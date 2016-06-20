from django.test import TestCase
from .forms import MemberForm

# Create your tests here.
class MemberFormTest(TestCase):

    def test_valid_data(self):
        form=MemberForm({'name':'Walter',
                            'paternalLastName':'Segama',
                            'maternalLastName': 'Segama',
                           'num_doc':77068833,
                            'phone':993904208,
                            'address':'av.universitaria',
                            'email':'correo@gmail.com'})
        self.assertTrue(form.is_valid())

    def test_empty_name(self):
        form = MemberForm({'name': '',
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

        form = MemberForm({'name': name,
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_numeric_name(self):
        form = MemberForm({'name': 12345,
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_empty_paternal_lastname(self):
        form = MemberForm({'name': 'Walter',
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

        form = MemberForm({'name': 'Walter',
                              'paternalLastName': name,
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_numeric_paternal_lastname(self):
        form = MemberForm({'name': 'Walter',
                              'paternalLastName': 12345,
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_empty_maternal_lastname(self):
        form = MemberForm({'name': 'Walter',
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

        form = MemberForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': name,
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_numeric_maternal_lastname(self):
        form = MemberForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 12345,
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_non_numeric_doc(self):
        form = MemberForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 'abcde',
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_empty_doc(self):
        form = MemberForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': '',
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_non_numeric_phone(self):
        form = MemberForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 'abcde',
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_empty_phone(self):
        form = MemberForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': '',
                              'address': 'av.universitaria',
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_empty_address(self):
        form = MemberForm({'name': 'Walter',
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

        form = MemberForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': address,
                              'email': 'correo@gmail.com'})
        self.assertFalse(form.is_valid())

    def test_empty_email(self):
        form = MemberForm({'name': 'Walter',
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

        form = MemberForm({'name': 'Walter',
                              'paternalLastName': 'Segama',
                              'maternalLastName': 'Segama',
                              'num_doc': 77068833,
                              'phone': 993904208,
                              'address': 'av.universitaria',
                              'email': email})
        self.assertFalse(form.is_valid())

