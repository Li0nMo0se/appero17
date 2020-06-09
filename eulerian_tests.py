import unittest
import snowymontreal
import solve_help


class IsEulerianTestCase(unittest.TestCase):
    def test_non_oriented_1(self):
        edges = [(0, 1, 0), (0, 2, 0), (0, 3, 0), (0, 4, 0), (1, 2, 0), (3, 1, 0), (4, 1, 0), (3, 2, 0), (2, 4, 0),
                 (4, 3, 0)]
        self.assertEqual(snowymontreal.is_eulerian_non_oriented(5, edges), True)

    def test_non_oriented_not_connected(self):
        edges = [(0, 2, 0), (2, 3, 0), (3, 0, 0), (2, 0, 0), (2, 1, 0), (3, 1, 0), (1, 2, 0)]
        self.assertEqual(snowymontreal.is_eulerian_non_oriented(4, edges), False)

    def test_non_oriented_empty(self):
        edges = []
        self.assertEqual(snowymontreal.is_eulerian_non_oriented(4, edges), True)

    def test_non_oriented_not_connected_2(self):
        edges = [(0, 1, 0), (2, 3, 0)]
        self.assertEqual(snowymontreal.is_eulerian_non_oriented(4, edges), False)


class IsEulerianCycleTestCase(unittest.TestCase):
    def test_eulerian_cycle_true(self):
        edges = [(0, 2, 0), (2, 3, 0), (3, 0, 0), (2, 0, 0), (2, 1, 0), (3, 1, 0), (1, 2, 0), (3, 2, 0), (0, 1, 0),
                 (0, 0, 0)]
        cycle = [0, 3, 2, 0, 0, 2, 1, 2, 3, 1]
        self.assertEqual(snowymontreal.is_eulerian_cycle(4, edges, cycle), True)

    def test_eulerian_cycle_false(self):
        edges = [(0, 2, 0), (2, 3, 0), (3, 0, 0), (2, 0, 0), (2, 1, 0), (3, 1, 0), (1, 2, 0), (3, 2, 0), (0, 1, 0)]
        cycle = [0, 3, 2, 0, 2, 1, 2, 1, 3]
        self.assertEqual(snowymontreal.is_eulerian_cycle(4, edges, cycle), False)

    def test_eulerian_cycle_one_edge(self):
        edges = [(1, 1, 0)]
        cycle = [1]
        self.assertEqual(snowymontreal.is_eulerian_cycle(2, edges, cycle), True)


class FindEulerianCycleTestCase(unittest.TestCase):
    def test_find_eulerian_cycle_non_oriented_short(self):
        g0 = (4, [(0, 1, 0), (1, 2, 0), (2, 3, 0), (3, 0, 0)])
        self.assertEqual(snowymontreal.is_eulerian_cycle(*g0,
                                                         snowymontreal.find_eulerian_cycle_non_oriented(*g0)), True)

    def test_find_eulerian_cycle_non_oriented_long(self):
        g1 = (4, [(2, 0, 0), (2, 1, 0), (3, 1, 0), (1, 2, 0), (0, 2, 0), (2, 3, 0), (3, 0, 0), (3, 2, 0), (0, 1, 0),
                  (0, 0, 0)])
        self.assertEqual(snowymontreal.is_eulerian_cycle(*g1,
                                                         snowymontreal.find_eulerian_cycle_non_oriented(*g1)), True)

    def test_find_eulerian_cycle_non_oriented_empty(self):
        g2 = (4, [])
        self.assertEqual(snowymontreal.is_eulerian_cycle(*g2,
                                                         snowymontreal.find_eulerian_cycle_non_oriented(*g2)), True)

    def test_find_eulerian_cycle_one_edge(self):
        g3 = (2, [(1, 1, 0)])
        self.assertEqual(snowymontreal.is_eulerian_cycle(*g3,
                                                         snowymontreal.find_eulerian_cycle_non_oriented(*g3)), True)


class OddVerticeTestCase(unittest.TestCase):
    def test_odd_vertice(self):
        self.assertEqual(snowymontreal.odd_vertices(4, [(0, 3, 0), (3, 2, 0), (1, 2, 0), (3, 1, 0)]), [0, 3], 0)

    def test_odd_vertice_2(self):
        self.assertEqual(snowymontreal.odd_vertices(3, [(1, 1, 0)]), [])


class IsConnectedTestCase(unittest.TestCase):
    def test_is_undirected_connected(self):
        self.assertEqual(solve_help.is_undirected_connected(4, [(0, 1, 0), (2, 1, 0), (3, 0, 0), (3, 1, 0)]), True)

    def test_is_undirected_connected_2(self):
        self.assertEqual(solve_help.is_undirected_connected(5, [(0, 1, 0), (2, 1, 0), (2, 0, 0), (4, 3, 0)]), False)


class IsEdgeConnectedTestCase(unittest.TestCase):
    def test_is_edge_undirected_connected(self):
        self.assertEqual(solve_help.is_edge_connected(5, [(0, 1, 0), (4, 1, 0), (3, 0, 0), (3, 1, 0)]), True)

    def test_is_edge_undirected_connected_2(self):
        self.assertEqual(solve_help.is_edge_connected(4, [(0, 1, 0), (3, 2, 0)]), False)

# TODO
class EulerizeTestCase(unittest.TestCase):
    pass

class SolveTestcase(unittest.TestCase):
    # TODO

    def test_solve_undirected_square(self):
        num_vertices = 5
        edges_list = [(0, 1, 3), (1, 2, 1), (2, 3, 6), (3, 0, 2), (0, 4, 8), (1, 4, 1), (2, 4, 3), (3, 4, 4)]
        cycle = snowymontreal.solve(False, num_vertices, edges_list)
        self.assertEqual(solve_help.is_eulerian_cycle(num_vertices, edges_list, cycle), True)


"""
    To run the unit tests, do 'python3 -m unittest eulerian_test.py'
"""

if __name__ == '__main__':
    unittest.main()
