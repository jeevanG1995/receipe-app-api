from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    
        def test_addition(self):
            res= calc.add(3, 8)
            self.assertEqual(res, 11)
    
        def test_adding_neg_number(self):
            sres= calc.add(3, -3)
            self.assertEqual(sres, 0)

        def test_subtract( self):
            res= calc.subtract(5, 11)
            self.assertEqual(res, 6)
