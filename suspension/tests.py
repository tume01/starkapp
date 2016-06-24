from django.test import TestCase
from .forms import SuspensionForms
from datetime import datetime
from datetime import timedelta

class SuspensionFormTest(TestCase):

    
    def test_valid_data(self):

        initialDate = datetime.now().date()
        finalDate = (datetime.now() + timedelta(days=1)).date()
        
        form = SuspensionForms({
            'reason' : 'Acumulación de multas sin pagar.',
            'initialDate' : initialDate,
            'finalDate': finalDate,
            })
        self.assertTrue(form.is_valid())

    def test_empty_reason(self):
        
        initialDate = datetime.now().date()
        finalDate = (datetime.now() + timedelta(days=1)).date()
        
        form = SuspensionForms({
            'reason' : '',
            'initialDate' : initialDate,
            'finalDate': finalDate,
            })
        self.assertFalse(form.is_valid())

    def test_long_reason(self):
        
        reason = ''
        for i in range(201):
            reason += 'a'

        initialDate = datetime.now().date()
        finalDate = (datetime.now() + timedelta(days=1)).date()
            
        form = SuspensionForms({
            'reason' : reason,
            'initialDate' : initialDate,
            'finalDate': finalDate,
            })
        self.assertFalse(form.is_valid())

    def test_empty_initialDate(self):

        initialDate = datetime.now().date()
        finalDate = (datetime.now() + timedelta(days=1)).date()
        
        form = SuspensionForms({
            'reason' : 'Acumulación de multas sin pagar.',
            'initialDate' : '',
            'finalDate': finalDate,
            })
        self.assertFalse(form.is_valid())

    def test_empty_initialDate(self):

        initialDate = (datetime.now() - timedelta(days=2)).date()
        finalDate = (datetime.now() - timedelta(days=1)).date()
        
        form = SuspensionForms({
            'reason' : 'Acumulación de multas sin pagar.',
            'initialDate' : initialDate,
            'finalDate': finalDate,
            })
        self.assertFalse(form.is_valid())

    def test_empty_finalDate(self):

        initialDate = datetime.now().date()
        finalDate = (datetime.now() + timedelta(days=1)).date()
        
        form = SuspensionForms({
            'reason' : 'Acumulación de multas sin pagar.',
            'initialDate' : initialDate,
            'finalDate': '',
            })
        self.assertFalse(form.is_valid())

