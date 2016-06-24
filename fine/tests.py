from django.test import TestCase
from .forms import FineForm, FineTypeForm

class FineTypeFormTest(TestCase):

    def test_valid_data(self):
        form = FineTypeForm({
            'reason':'Daños materiales',
            'price':100
            })
        self.assertTrue(form.is_valid())

    def test_empty_reason(self):
        
        form = FineTypeForm({
            'reason':'',
            'price':100
            })
        self.assertFalse(form.is_valid())

    def test_long_reason(self):
        reason = ''
        for i in range(201):
            reason += 'a'

        form = FineTypeForm({
            'reason':reason,
            'price':100
            })
        self.assertFalse(form.is_valid())

    def test_empty_price(self):
        
        form = FineTypeForm({
            'reason':'Daños materiales',
            'price':''
            })
        self.assertFalse(form.is_valid())

class FineFormTest(TestCase):

    def test_valid_data(self):
        form = FineForm({
            'observations':'Rompio algo'
            })
        self.assertTrue(form.is_valid())

    def test_empty_observation(self):
        form = FineForm({
            'observations':''
            })
        self.assertFalse(form.is_valid())

    def test_long_observation(self):
        observation = ''
        for i in range(201):
            observation += 'a'
        
        form = FineForm({
            'observations':observation
            })
        self.assertFalse(form.is_valid())

    
        
