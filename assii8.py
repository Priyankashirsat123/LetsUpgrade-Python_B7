import unittest
class TestStringMethods(unittest.TestCase):
   def test_upper(self):
      self.assertEqual('TUTOR'.lower(), 'tutor')
   def test_islower(self):
      self.assertTrue('tutor'.islower())
      self.assertFalse('Tutor'.islower())
if __name__ == '__main__':
   unittest.main()
