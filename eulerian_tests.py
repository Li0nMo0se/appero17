import unittest
from solve import *


class MyTestCase(unittest.TestCase):
    def test_is_eulerian_non_oriented(self):
        edges = [(0, 1, 0), (0, 2, 0), (0, 3, 0), (0, 4, 0), (1, 2, 0), (3, 1, 0), (4, 1, 0), (3, 2, 0), (2, 4, 0),
                 (4, 3, 0)]
        self.assertEqual(is_eulerian_non_oriented(5, edges), True)


if __name__ == '__main__':
    unittest.main()
