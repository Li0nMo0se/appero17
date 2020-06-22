import unittest
import snowymontreal as sm
import snowymontreal.solve_aux as sa


class IsEulerianTestCase(unittest.TestCase):
    def test_non_oriented_1(self):
        edges = [(0, 1, 0), (0, 2, 0), (0, 3, 0), (0, 4, 0), (1, 2, 0),
                 (3, 1, 0), (4, 1, 0), (3, 2, 0), (2, 4, 0), (4, 3, 0)]
        self.assertEqual(True, sa.is_eulerian(5, edges, is_oriented=False))

    def test_non_oriented_not_connected(self):
        edges = [(0, 2, 0), (2, 3, 0), (3, 0, 0), (2, 0, 0), (2, 1, 0),
                 (3, 1, 0), (1, 2, 0)]
        self.assertEqual(False, sa.is_eulerian(4, edges, is_oriented=False))

    def test_non_oriented_empty(self):
        edges = []
        self.assertEqual(True, sa.is_eulerian(4, edges, is_oriented=False))

    def test_non_oriented_not_connected_2(self):
        edges = [(0, 1, 0), (2, 3, 0)]
        self.assertEqual(False, sa.is_eulerian(4, edges, is_oriented=False))

    def test_oriented_true(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        self.assertEqual(True, sa.is_eulerian(num_vertices, edges_list,
                                              is_oriented))

    def test_oriented_false(self):
        is_oriented = True
        num_vertices = 6
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5),
                      (0, 5, 1)]
        self.assertEqual(False, sa.is_eulerian(num_vertices, edges_list,
                                               is_oriented))


class IsEulerianCycleTestCase(unittest.TestCase):
    def test_eulerian_cycle_true(self):
        edges = [(0, 2, 0), (2, 3, 0), (3, 0, 0), (2, 0, 0), (2, 1, 0),
                 (3, 1, 0), (1, 2, 0), (3, 2, 0), (0, 1, 0), (0, 0, 0)]
        cycle = [0, 3, 2, 0, 0, 2, 1, 2, 3, 1]
        self.assertEqual(True, sa.is_eulerian_cycle(4, edges, False, cycle))

    def test_eulerian_cycle_false(self):
        edges = [(0, 2, 0), (2, 3, 0), (3, 0, 0), (2, 0, 0), (2, 1, 0),
                 (3, 1, 0), (1, 2, 0), (3, 2, 0), (0, 1, 0)]
        cycle = [0, 3, 2, 0, 2, 1, 2, 1, 3]
        self.assertEqual(False, sa.is_eulerian_cycle(4, edges, False, cycle))

    def test_eulerian_cycle_one_edge(self):
        edges = [(1, 1, 0)]
        cycle = [1]
        self.assertEqual(True, sa.is_eulerian_cycle(2, edges, False, cycle))

    def test_eulerian_cycle_directed(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        cycle = [0, 1, 2, 3, 4]
        self.assertEqual(True, sa.is_eulerian_cycle(num_vertices, edges_list,
                                                    is_oriented, cycle))

    def test_eulerian_not_cycle_directed(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        cycle = [1, 2, 3, 0, 4]
        self.assertEqual(False, sa.is_eulerian_cycle(num_vertices, edges_list,
                                                     is_oriented, cycle))


class FindEulerianCycleTestCase(unittest.TestCase):
    def test_find_eulerian_cycle_non_oriented_short(self):
        g = (4, [(0, 1, 0), (1, 2, 0), (2, 3, 0), (3, 0, 0)], False)
        self.assertEqual(True, sa.is_eulerian_cycle(*g,
                                                    sa.find_eulerian_cycle(*g)))

    def test_find_eulerian_cycle_non_oriented_long(self):
        g = (4, [(2, 0, 0), (2, 1, 0), (3, 1, 0), (1, 2, 0), (0, 2, 0),
                 (2, 3, 0), (3, 0, 0), (3, 2, 0), (0, 1, 0),
                 (0, 0, 0)], False)
        self.assertEqual(True, sa.is_eulerian_cycle(*g,
                                                    sa.find_eulerian_cycle(*g)))

    def test_find_eulerian_cycle_non_oriented_empty(self):
        g = (4, [], False)
        self.assertEqual(True, sa.is_eulerian_cycle(*g,
                                                    sa.find_eulerian_cycle(*g)))

    def test_find_eulerian_cycle_one_edge(self):
        g = (2, [(1, 1, 0)], False)
        self.assertEqual(True, sa.is_eulerian_cycle(*g,
                                                    sa.find_eulerian_cycle(*g)))

    def test_find_eulerian_cycle_directed(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        g = (num_vertices, edges_list, is_oriented)
        self.assertEqual(True, sa.is_eulerian_cycle(*g,
                                                    sa.find_eulerian_cycle(*g)))

    def test_find_eulerian_bug_fixed(self):
        is_oriented = False
        edges_list =\
            [(0, 29, 355.427), (1, 6, 864.748), (1, 29, 296.667),
             (2, 17, 710.343), (2, 21, 661.4780000000001), (2, 5, 542.428),
             (2, 19, 933.705), (3, 9, 9.612), (3, 26, 1011.4849999999999),
             (3, 18, 1173.4869999999999), (4, 18, 20.198), (4, 17, 243.967),
             (4, 23, 611.3299999999998), (5, 11, 869.11), (6, 26, 3.155),
             (7, 14, 25.393), (7, 9, 211.382), (7, 10, 110.475),
             (8, 10, 216.413), (9, 10, 168.06900000000002), (11, 12, 281),
             (13, 14, 176), (15, 18, 247), (16, 17, 271.433), (19, 20, 314.212),
             (21, 24, 1493.3), (22, 24, 261.903), (23, 25, 294.418),
             (23, 26, 954.615), (24, 25, 60.786), (25, 27, 215.65300000000002),
             (28, 29, 275.92), (0, 29, 355.427), (29, 1, 296.667),
             (1, 6, 864.748), (6, 26, 3.155), (26, 3, 1011.4849999999999),
             (4, 18, 20.198), (18, 3, 1173.4869999999999), (3, 9, 9.612),
             (9, 7, 211.382), (8, 10, 216.413), (10, 9, 168.06900000000002),
             (10, 9, 168), (9, 3, 9.612), (3, 18, 1173), (18, 4, 20.198),
             (4, 17, 243.967), (17, 2, 710.343), (2, 5, 542.428), (5, 11, 869),
             (11, 12, 281), (13, 14, 176), (14, 7, 25.393), (7, 9, 211.382),
             (9, 3, 9.612), (3, 18, 1173), (18, 15, 247), (16, 17, 271.433),
             (18, 4, 20.198), (4, 17, 243.967), (17, 2, 710.343), (2, 19, 933),
             (19, 20, 314.212), (22, 24, 261.903), (24, 25, 60), (25, 23, 294),
             (24, 25, 60.786), (26, 23, 954.615), (23, 25, 294.418),
             (25, 27, 215), (28, 29, 275.92)]
        num_vertices = 30
        g = (num_vertices, edges_list, is_oriented)
        self.assertEqual(True, sa.is_eulerian_cycle(*g,
                                                    sa.find_eulerian_cycle(*g)))

class OddVerticeTestCase(unittest.TestCase):
    def test_odd_vertices_undirected(self):
        g = (4, [(0, 3, 0), (3, 2, 0), (1, 2, 0), (3, 1, 0)])
        self.assertEqual([0, 3], sa.odd_vertices_undirected(*g))

    def test_odd_vertices_undirected_2(self):
        g = (3, [(1, 1, 0)])
        self.assertEqual(True, sa.test_vertices_eulerian(*g))

    def test_odd_vertices_directed_already_eulerian(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        self.assertEqual(True, sa.test_vertices_eulerian(
            num_vertices, edges_list, is_oriented=is_oriented))


class IsConnectedTestCase(unittest.TestCase):
    def test_is_undirected_connected(self):
        edges_list = [(0, 1, 0), (2, 1, 0), (3, 0, 0), (3, 1, 0)]
        self.assertEqual(sa.is_connected(4, edges_list, False), True)

    def test_is_undirected_connected_2(self):
        edges_list = [(0, 1, 0), (2, 1, 0), (2, 0, 0), (4, 3, 0)]
        self.assertEqual(sa.is_connected(5, edges_list, False), False)

    def test_is_directed_eulerian_connected(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        self.assertEqual(sa.is_connected(num_vertices, edges_list,
                                         is_oriented=is_oriented), True)

    def test_is_directed_eulerian_not_connected(self):
        is_oriented = True
        num_vertices = 6
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        self.assertEqual(sa.is_connected(num_vertices, edges_list,
                                         is_oriented=is_oriented), False)


class IsEdgeConnectedTestCase(unittest.TestCase):
    def test_is_edge_undirected_connected(self):
        self.assertEqual(sa.is_edge_connected(5, [(0, 1, 0), (4, 1, 0),
                                                  (3, 0, 0), (3, 1, 0)]), True)

    def test_is_edge_undirected_connected_2(self):
        self.assertEqual(sa.is_edge_connected(4, [(0, 1, 0), (3, 2, 0)]), False)


class EulerizeTestCase(unittest.TestCase):
    def test_eulerize_undirected(self):
        edges_list = [(0, 2, 0), (0, 4, 3), (0, 5, 0), (1, 4, 2), (1, 5, 1),
                      (2, 3, 4), (2, 4, 3), (4, 5, 1)]
        num_vertices = 6
        sa.eulerize(num_vertices, edges_list, is_oriented=False)
        self.assertEqual(True, sa.is_eulerian(num_vertices, edges_list,
                                              is_oriented=False))

    def test_eulerize_undirected_2(self):
        edges_list = [(0, 1, 0), (1, 2, 3), (2, 3, 0), (3, 0, 2), (0, 4, 2),
                      (1, 4, 4), (2, 4, 0), (3, 4, 3)]
        num_vertices = 5
        sa.eulerize(num_vertices, edges_list, is_oriented=False)
        self.assertEqual(True, sa.is_eulerian(num_vertices, edges_list,
                                              is_oriented=False))

    def test_eulerize_directed(self):
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5),
                      (0, 5, 7), (5, 0, 7), (0, 4, 5), (3, 2, 3)]
        num_vertices = 6
        sa.eulerize(num_vertices, edges_list, is_oriented=True)
        self.assertEqual(True, sa.is_eulerian(num_vertices,
                                              edges_list, is_oriented=True))

    def test_eulerize_undirected_3(self):
        edges_list = [(0, 1, 7), (1, 2, 6), (2, 3, 9), (3, 0, 8), (0, 4, 4),
                      (1, 4, 2), (2, 4, 3), (3, 4, 5)]
        num_vertices = 6
        sa.eulerize(num_vertices, edges_list, is_oriented=False)
        self.assertEqual(True, sa.is_eulerian(num_vertices, edges_list,
                                              is_oriented=False))

class IsValidTestCase(unittest.TestCase):
    def test_is_valid_true(self):
        is_oriented = False
        num_vertices = 6
        edges_list = [(0, 1, 1), (0, 3, 1), (0, 4, 4), (1, 2, 2), (1, 4, 3),
                      (2, 5, 1), (3, 4, 2), (4, 5, 1), (5, 2, 56)]
        path = [5, 4, 0, 1, 4, 3, 0, 1, 2, 5, 2]
        self.assertEqual(True, sa.is_valid(num_vertices, edges_list,
                                           is_oriented, path))

    def test_is_valid_false(self):
        is_oriented = False
        num_vertices = 6
        edges_list = [(0, 1, 1), (0, 3, 1), (0, 4, 4), (1, 2, 2), (1, 4, 3),
                      (2, 5, 1), (3, 4, 2), (4, 5, 1), (5, 2, 56), (5, 2, 1),
                      (2, 5, 1)]
        path = [5, 4, 0, 1, 4, 3, 0, 1, 2, 5, 2]
        self.assertEqual(False, sa.is_valid(num_vertices, edges_list,
                                            is_oriented, path))

    def test_is_valid_empty(self):
        is_oriented = True
        num_vertices = 1
        edges_list = []
        path = []
        self.assertEqual(True, sa.is_valid(num_vertices, edges_list,
                                           is_oriented, path))

    def test_is_valid_one_edge(self):
        is_oriented = True
        num_vertices = 1
        edges_list = [(1, 1, 0)]
        path = [1]
        self.assertEqual(True, sa.is_valid(num_vertices, edges_list,
                                           is_oriented, path))

    def test_is_valid_one_edge_two_vertices(self):
        is_oriented = True
        num_vertices = 2
        edges_list = [(1, 1, 0)]
        path = [1]
        self.assertEqual(True, sa.is_valid(num_vertices, edges_list,
                                           is_oriented, path))


class SolveTestcase(unittest.TestCase):
    def test_solve_already_undirected_eulerian(self):
        is_oriented = False
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sa.is_valid(num_vertices, edges_list,
                                     is_oriented, cycle), True)

    def test_solve_already_directed_eulerian(self):
        is_oriented = True
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 0, 5)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sa.is_valid(num_vertices, edges_list,
                                     is_oriented, cycle), True)

    def test_solve_undirected_square(self):
        is_oriented = False
        num_vertices = 5
        edges_list = [(0, 1, 3), (1, 2, 1), (2, 3, 6), (3, 0, 2), (0, 4, 8),
                      (1, 4, 1), (2, 4, 3), (3, 4, 4)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sa.is_valid(num_vertices, edges_list,
                                     is_oriented, cycle), True)

    def test_solve_undirected_1(self):
        is_oriented = False
        num_vertices = 6
        edges_list = [(0, 1, 1), (0, 3, 1), (0, 4, 4), (1, 2, 2), (1, 4, 3),
                      (2, 5, 1), (3, 4, 2), (4, 5, 1), (5, 2, 56)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sa.is_valid(num_vertices, edges_list,
                                     is_oriented, cycle), True)

    def test_solve_undirected_2(self):
        is_oriented = False
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 0, 3), (3, 2, 1), (1, 4, 4), (4, 3, 2),
                      (3, 4, 2)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sa.is_valid(num_vertices, edges_list,
                                     is_oriented, cycle), True)

    def test_solve_undirected_3(self):
        is_oriented = False
        num_vertices = 4
        edges_list = [(0, 3, 2), (0, 1, 1), (1, 2, 12), (2, 0, 4)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sa.is_valid(num_vertices, edges_list,
                                     is_oriented, cycle), True)

    def test_solve_undirected_4(self):
        is_oriented = False
        num_vertices = 5
        edges_list = [(0, 1, 7), (1, 0, 3), (3, 2, 1), (1, 4, 4), (4, 3, 3),
                      (3, 4, 2), (0, 3, 1)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sa.is_valid(num_vertices, edges_list,
                                     is_oriented, cycle), True)

    def test_solve_undirected_5(self):
        is_oriented = False
        num_vertices = 9
        edges_list = [(1, 2, 3), (1, 7, 8), (2, 3, 6), (2, 4, 4), (3, 4, 1),
                      (3, 5, 2), (3, 7, 1), (4, 8, 4), (5, 6, 3), (5, 0, 1),
                      (6, 0, 2), (6, 7, 6)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sa.is_valid(num_vertices, edges_list,
                                     is_oriented, cycle), True)

    def test_solve_undirected_6(self):
        is_oriented = False
        num_vertices = 5
        edges_list = [(0, 1, 1), (1, 2, 3), (2, 3, 2), (3, 0, 2), (1, 4, 1),
                      (4, 2, 4), (0, 3, 1)]
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sa.is_valid(num_vertices, edges_list,
                                     is_oriented, cycle), True)

    def test_undirected_bug(self):
        is_oriented = False
        edges_list =\
            [(0, 29, 355), (1, 6, 864), (1, 29, 296), (2, 17, 710),
             (2, 21, 661), (2, 5, 542), (2, 19, 933), (3, 9, 9), (3, 26, 1011),
             (3, 18, 1173), (4, 18, 20.198), (4, 17, 243.967), (4, 23, 611),
             (5, 11, 869), (6, 26, 3), (7, 14, 25), (7, 9, 211), (7, 10, 110),
             (8, 10, 216), (9, 10, 168), (11, 12, 281), (13, 14, 176),
             (15, 18, 247), (16, 17, 271.433), (19, 20, 314), (21, 24, 1493),
             (22, 24, 261.903), (23, 25, 294.418), (23, 26, 954.615),
             (24, 25, 60.786), (25, 27, 215), (28, 29, 275.92)]
        num_vertices = 30
        cycle = sm.solve(is_oriented, num_vertices, edges_list)
        self.assertEqual(sa.is_valid(num_vertices, edges_list,
                                     is_oriented, cycle), True)


"""
    To run the unit tests, do 'python3 -m unittest eulerian_test.py'
"""

if __name__ == '__main__':
    unittest.main()
