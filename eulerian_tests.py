import unittest
from solve import *


class MyTestCase(unittest.TestCase):
    def test_is_eulerian_non_oriented(self):
        edges = [(0, 1, 0), (0, 2, 0), (0, 3, 0), (0, 4, 0), (1, 2, 0), (3, 1, 0), (4, 1, 0), (3, 2, 0), (2, 4, 0),
                 (4, 3, 0)]
        self.assertEqual(is_eulerian_non_oriented(5, edges), True)
    def test_even_vertices(self):
        edges = [(0,2),(2,3),(3,0),(2,0),(0,1),(0,0)]

        self.assertEqual(even_vertices(4,edges),False);
    def test_find_eulerian_cycle_not_oriented(self):
        edges = [(0,1),(1,2),(2,3),(3,0)]

        self.assertEqual(find_eulerian_cycle_non_oriented(4,edges),True);


if __name__ == '__main__':
    unittest.main()
