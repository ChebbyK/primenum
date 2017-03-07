import unittest
from primenum import primenum
 
class TestPrimenum (unittest.TestCase):
    def test_primenum(self):
      self.assertListEqual([5,7], primenum())

class TestPrimenum (unittest.TestCase):
      def test_add(self):
        self.assertTrue(addnum (5,7,"+"),12)

class TestPrimenum (unittest.TestCase):
      def test_evennum(self):
        self.assertEqual([6,8], evennum())

class TestPrimenum (unittest.TestCase):
      def test_oddnum(self):
        self.assertEqual([3,5], oddnum())

class TestPrimenum (unittest.TestCase):
      def test_multiply(self):
        self.assertTrue(multiply (2,6,"*"),12)


if __name__ == "__main__":
    unittest.main()
