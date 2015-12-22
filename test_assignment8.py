import unittest
from assignment8 import fib

class TestAssignment8(unittest.TestCase):
	def test_fib_func(self) :
		self.assertEqual(fib().next() , 1)


if __name__ == '__main__':
    unittest.main()

