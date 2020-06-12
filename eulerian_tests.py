import unittest
import snowymontreal as sm


class IsEulerianTestCase(unittest.TestCase):
    def test_non_oriented_1(self):
        edges = [(0, 1, 0), (0, 2, 0), (0, 3, 0), (0, 4, 0), (1, 2, 0),
                 (3, 1, 0), (4, 1, 0), (3, 2, 0), (2, 4, 0), (4, 3, 0)]
        self.assertEqual(True, sm.is_eulerian(5, edges, is_oriented=False))

    def test_non_oriented_not_connected(self):
        edges = [(0, 2, 0), (2, 3, 0), (3, 0, 0), (2, 0, 0), (2, 1, 0),
                 (3, 1, 0), (1, 2, 0)]
        self.assertEqual(False, sm.is_eulerian(4, edges, is_oriented=False))

    def test_non_oriented_empty(self):
        edges = []
        self.assertEqual(True, sm.is_eulerian(4, edges, is_oriented=False))

    def test_non_oriented_not_connected_2(self):
        edges = [(0, 1, 0), (2, 3, 0)]
        self.assertEqual(False, sm.is_eulerian(4, edges, is_oriented=False))

    def test_oriented_true(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        self.assertEqual(True, sm.is_eulerian(num_vertices, edges_list,
                                              is_oriented))

    def test_oriented_false(self):
        is_oriented = True
        num_vertices = 6
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5),
                      (0, 5, 1)]
        self.assertEqual(False, sm.is_eulerian(num_vertices, edges_list,
                                               is_oriented))


class IsEulerianCycleTestCase(unittest.TestCase):
    def test_eulerian_cycle_true(self):
        edges = [(0, 2, 0), (2, 3, 0), (3, 0, 0), (2, 0, 0), (2, 1, 0),
                 (3, 1, 0), (1, 2, 0), (3, 2, 0), (0, 1, 0), (0, 0, 0)]
        cycle = [0, 3, 2, 0, 0, 2, 1, 2, 3, 1]
        self.assertEqual(True, sm.is_eulerian_cycle(4, edges, False, cycle))

    def test_eulerian_cycle_false(self):
        edges = [(0, 2, 0), (2, 3, 0), (3, 0, 0), (2, 0, 0), (2, 1, 0),
                 (3, 1, 0), (1, 2, 0), (3, 2, 0), (0, 1, 0)]
        cycle = [0, 3, 2, 0, 2, 1, 2, 1, 3]
        self.assertEqual(False, sm.is_eulerian_cycle(4, edges, False, cycle))

    def test_eulerian_cycle_one_edge(self):
        edges = [(1, 1, 0)]
        cycle = [1]
        self.assertEqual(True, sm.is_eulerian_cycle(2, edges, False, cycle))

    def test_eulerian_cycle_directed(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        cycle = [0, 1, 2, 3, 4]
        self.assertEqual(True, sm.is_eulerian_cycle(num_vertices, edges_list,
                                                    is_oriented, cycle))

    def test_eulerian_not_cycle_directed(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        cycle = [1, 2, 3, 0, 4]
        self.assertEqual(False, sm.is_eulerian_cycle(num_vertices, edges_list,
                                                     is_oriented, cycle))


class FindEulerianCycleTestCase(unittest.TestCase):
    def test_find_eulerian_cycle_non_oriented_short(self):
        g = (4, [(0, 1, 0), (1, 2, 0), (2, 3, 0), (3, 0, 0)], False)
        self.assertEqual(True, sm.is_eulerian_cycle(*g,
                                              sm.find_eulerian_cycle(*g)))

    def test_find_eulerian_cycle_non_oriented_long(self):
        g = (4, [(2, 0, 0), (2, 1, 0), (3, 1, 0), (1, 2, 0), (0, 2, 0),
                  (2, 3, 0), (3, 0, 0), (3, 2, 0), (0, 1, 0),
                  (0, 0, 0)], False)
        self.assertEqual(True, sm.is_eulerian_cycle(*g,
                                                   sm.find_eulerian_cycle(*g)))

    def test_find_eulerian_cycle_non_oriented_empty(self):
        g = (4, [], False)
        self.assertEqual(True, sm.is_eulerian_cycle(*g,
                                                    sm.find_eulerian_cycle(*g)))

    def test_find_eulerian_cycle_one_edge(self):
        g = (2, [(1, 1, 0)], False)
        self.assertEqual(True, sm.is_eulerian_cycle(*g,
                                                    sm.find_eulerian_cycle(*g)))

    def test_find_eulerian_cycle_directed(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        g = (num_vertices, edges_list, is_oriented)
        self.assertEqual(True, sm.is_eulerian_cycle(*g,
                                                    sm.find_eulerian_cycle(*g)))


class OddVerticeTestCase(unittest.TestCase):
    def test_odd_vertices_undirected(self):
        g = (4, [(0, 3, 0), (3, 2, 0), (1, 2, 0), (3, 1, 0)])
        self.assertEqual([0, 3], sm.odd_vertices_undirected(*g))

    def test_odd_vertices_undirected_2(self):
        g = (3, [(1, 1, 0)])
        self.assertEqual(True, sm.test_vertices_eulerian(*g))

    def test_odd_vertices_directed_already_eulerian(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        self.assertEqual(True, sm.test_vertices_eulerian(
            num_vertices, edges_list, is_oriented=is_oriented))


class IsConnectedTestCase(unittest.TestCase):
    def test_is_undirected_connected(self):
        edges_list = [(0, 1, 0), (2, 1, 0), (3, 0, 0), (3, 1, 0)]
        self.assertEqual(sm.is_connected(4, edges_list, False), True)

    def test_is_undirected_connected_2(self):
        edges_list = [(0, 1, 0), (2, 1, 0), (2, 0, 0), (4, 3, 0)]
        self.assertEqual(sm.is_connected(5, edges_list, False), False)

    def test_is_directed_eulerian_connected(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        self.assertEqual(sm.is_connected(num_vertices, edges_list,
                                                is_oriented=is_oriented), True)

    def test_is_directed_eulerian_not_connected(self):
        is_oriented = True
        num_vertices = 6
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        self.assertEqual(sm.is_connected(num_vertices, edges_list,
                                                is_oriented=is_oriented), False)


class IsEdgeConnectedTestCase(unittest.TestCase):
    def test_is_edge_undirected_connected(self):
        self.assertEqual(sm.is_edge_connected(5, [(0, 1, 0), (4, 1, 0),
                                                  (3, 0, 0), (3, 1, 0)]), True)

    def test_is_edge_undirected_connected_2(self):
        self.assertEqual(sm.is_edge_connected(4, [(0, 1, 0), (3, 2, 0)]), False)


class EulerizeTestCase(unittest.TestCase):
    def test_eulerize_undirected(self):
        edges_list = [(0, 2, 0), (0, 4, 3), (0, 5, 0), (1, 4, 2), (1, 5, 1),
                      (2, 3, 4), (2, 4, 3), (4, 5, 1)]
        num_vertices = 6
        sm.eulerize(num_vertices, edges_list, is_oriented=False)
        self.assertEqual(True, sm.is_eulerian(num_vertices, edges_list,
                                              is_oriented=False))

    def test_eulerize_undirected_2(self):
        edges_list = [(0, 1, 0), (1, 2, 3), (2, 3, 0), (3, 0, 2),(0, 4, 2),
                      (1, 4, 4), (2, 4, 0), (3, 4, 3)]
        num_vertices = 5
        sm.eulerize(num_vertices, edges_list, is_oriented=False)
        self.assertEqual(True, sm.is_eulerian(num_vertices, edges_list,
                                              is_oriented=False))

    def test_eulerize_directed(self):
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5),
                      (0, 5, 7), (5, 0, 7), (0, 4, 5), (3, 2, 3)]
        num_vertices = 6
        sm.eulerize(num_vertices, edges_list, is_oriented=True)
        self.assertEqual(True, sm.is_eulerian(num_vertices,
                                              edges_list, is_oriented=True))
    def test_eulerize_undirected_3(self):
        edges_list = [(0, 1, 7), (1, 2, 6), (2, 3, 9), (3, 0, 8), (0, 4, 4),
                      (1, 4, 2), (2, 4, 3), (3, 4, 5)]
        num_vertices = 6
        sm.eulerize(num_vertices, edges_list, is_oriented=False)
        self.assertEqual(True, sm.is_eulerian(num_vertices, edges_list,
                                              is_oriented=False))
class SolveTestcase(unittest.TestCase):
    def test_solve_already_undirected_eulerian(self):
        is_oriented = False
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sm.is_eulerian_cycle(num_vertices, edges_list,
                                              is_oriented, cycle), True)

    def test_solve_already_directed_eulerian(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sm.is_eulerian_cycle(num_vertices, edges_list,
                                              is_oriented, cycle), True)

    def test_solve_undirected_square(self):
        is_oriented = False
        num_vertices = 5
        edges_list = [(0, 1, 3), (1, 2, 1), (2, 3, 6), (3, 0, 2), (0, 4, 8),
                      (1, 4, 1), (2, 4, 3), (3, 4, 4)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sm.is_eulerian_cycle(num_vertices, edges_list,
                                              is_oriented, cycle), True)

    def test_solve_undirected_1(self):
        is_oriented = False
        num_vertices = 6
        edges_list = [(0, 1, 1), (0, 3, 1), (0, 4, 4), (1, 2, 2), (1, 4, 3),
                      (2, 5, 1), (3, 4, 2), (4, 5, 1), (5, 2, 56)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sm.is_eulerian_cycle(num_vertices, edges_list,
                                              is_oriented, cycle), True)

    def test_solve_undirected_2(self):
        is_oriented = False
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 0, 3), (3, 2, 1), (1, 4, 4), (4, 3, 2),
                      (3, 4, 2)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sm.is_eulerian_cycle(num_vertices, edges_list,
                                              is_oriented, cycle), True)

    def test_solve_undirected_3(self):
        is_oriented = False
        num_vertices = 4
        edges_list = [(0, 3, 2), (0, 1, 1), (1, 2, 12), (2, 0, 4)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sm.is_eulerian_cycle(num_vertices, edges_list,
                                              is_oriented, cycle), True)

    def test_solve_undirected_4(self):
        is_oriented = False
        num_vertices = 5
        edges_list = [(0, 1, 7), (1, 0, 3), (3, 2, 1), (1, 4, 4), (4, 3, 3),
                      (3, 4, 2), (0, 3, 1)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sm.is_eulerian_cycle(num_vertices, edges_list,
                                              is_oriented, cycle), True)

    def test_solve_undirected_5(self):
        is_oriented = False
        num_vertices = 9
        edges_list = [(1, 2, 3), (1, 7, 8), (2, 3, 6), (2, 4, 4), (3, 4, 1),
                      (3, 5, 2), (3, 7, 1), (4, 8, 4), (5, 6, 3), (5, 0, 1),
                      (6, 0, 2), (6, 7, 6)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sm.is_eulerian_cycle(num_vertices, edges_list,
                                              is_oriented, cycle), True)

    def test_solve_undirected_6(self):
        is_oriented = False
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 3), (2, 3, 2), (3, 0, 2), (1, 4, 1),
                      (4, 2, 4), (0, 3, 1)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sm.is_eulerian_cycle(num_vertices, edges_list,
                                              is_oriented, cycle), True)


"""
    To run the unit tests, do 'python3 -m unittest eulerian_test.py'
"""

if __name__ == '__main__':
    unittest.main()
