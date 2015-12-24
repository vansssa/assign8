import unittest
from assignment8 import fib


class TestAssignment8(unittest.TestCase):

    def setUp(self):
        self.myfib = fib()

    def test_fib_func(self):
        solution_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in solution_list:
            self.assertEqual(self.myfib.next(), i)


if __name__ == '__main__':
    unittest.main()
