import unittest
from solve import *


class IsEulerianTestCase(unittest.TestCase):
    def test_non_oriented_1(self):
        edges = [(0, 1, 0), (0, 2, 0), (0, 3, 0), (0, 4, 0), (1, 2, 0), (3, 1, 0), (4, 1, 0), (3, 2, 0), (2, 4, 0),
                 (4, 3, 0)]
        self.assertEqual(is_eulerian_non_oriented(5, edges), True)

    def test_non_oriented_not_connected(self):
        edges = [(0, 2, 0), (2, 3, 0), (3, 0, 0), (2, 0, 0), (2, 1, 0), (3, 1, 0), (1, 2, 0)]
        self.assertEqual(is_eulerian_non_oriented(4, edges), False)

    def test_non_oriented_empty(self):
        edges = []
        self.assertEqual(is_eulerian_non_oriented(4, edges), True)

    def test_non_oriented_not_connected_2(self):
        edges = [(0, 1, 0), (2, 3, 0)]
        self.assertEqual(is_eulerian_non_oriented(4, edges), False)
'''
    Cheick, fais une classe par fonction comme ca c'est plus clair
    Les fonctions de test doivent obligatoirement commence par test_*
    
    Enfin, pour lancer la test suite il faut que tu fasses python3 -m unittest eulerian_tests.py
'''

if __name__ == '__main__':
    unittest.main()
