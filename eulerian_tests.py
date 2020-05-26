import unittest
from solve import *
'''from solve_help import *
'''
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


class IsEulerianCycleTestCase(unittest.TestCase):
    def test_eulerian_cycle_true(self):
        edges = [(0,2),(2,3),(3,0),(2,0),(2,1),(3,1),(1,2),(3,2),(0,1),(0,0)]
        cycle = [0,3,2,0,0,2,1,2,3,1]
        self.assertEqual(is_eulerian_cycle(4, edges, cycle), True)
    
    def test_eulerian_cycle_false(self):
        edges = [(0,2),(2,3),(3,0),(2,0),(2,1),(3,1),(1,2),(3,2),(0,1)]
        cycle = [0,3,2,0,2,1,2,1,3]
        self.assertEqual(is_eulerian_cycle(4, edges, cycle), False)


class FindEulerianCycleTestCase(unittest.TestCase):
    def test_find_eulerian_cycle_non_oriented_short(self):
        g0 = (4, [(0,1),(1,2),(2,3),(3,0)])
        self.assertEqual(is_eulerian_cycle(*g0, find_eulerian_cycle_non_oriented(*g0)), True)

    def test_find_eulerian_cycle_non_oriented_long(self):
        g1=(4, [(2,0),(2,1),(3,1),(1,2),(0,2),(2,3),(3,0),(3,2),(0,1),(0,0)])
        self.assertEqual(is_eulerian_cycle(*g1, find_eulerian_cycle_non_oriented(*g1)), True)

    def test_find_eulerian_cycle_non_oriented_empty(self):
        g2 = (4, [])
        self.assertEqual(is_eulerian_cycle(*g2, find_eulerian_cycle_non_oriented(*g2)), True)

class OddVerticeTestCase(unittest.TestCase):
    def test_odd_vertice(self):
        self.assertEqual(odd_vertices(4, [(0,3),(3,2),(1,2),(3,1)]), [0, 3]) 

    def test_odd_vertice_2(self):
        self.assertEqual(odd_vertices(3, [(1,1)]), [])


class SolveTestcase(unittest.TestCase):
    ''' TODO '''
    


'''    
    Pour lancer la test suite il faut faire python3 -m unittest eulerian_tests.py
'''

if __name__ == '__main__':
    unittest.main()
