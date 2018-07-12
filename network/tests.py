import unittest
from network import critical_place_count

class TestNetwork(unittest.TestCase):

    def test1_no_critical_places(self):
        """Network with no critical places. (1p)"""
        network = [
            (1, 2),
            (0, 2),
            (0, 1)
        ]
        #     0
        #   /   \
        #  1 ___ 2
        #  No critical places
        self.assertEqual(0, critical_place_count(network))

    def test2_one_critical_place(self):
        """Network with one critical place. (1p)"""
        network = [
            (1, 2),
            (0, 2),
            (0, 1, 3),
            (2,)
        ]
        #     0
        #   /   \
        #  1 ___ 2
        #         \
        #          3
        # One critical place: 2
        self.assertEqual(1, critical_place_count(network))

    def test3_two_critical_place(self):
        """Network with two critical places. (1p)"""
        network = [
            (1, 2),
            (0, 2, 4),
            (0, 1, 3),
            (2,),
            (1,)
        ]
        #  4    0
        #   \ /   \
        #    1 ___ 2
        #           \
        #            3
        # Two critical places: 1, 2
        self.assertEqual(2, critical_place_count(network))

    def test4_three_critical_place(self):
        """Network with three critical places. (1p)"""
        network = [
            (1, 2),
            (0, 2, 4),
            (0, 1, 3),
            (2, 5),
            (1,),
            (3,)
        ]
        #  4    0
        #   \ /   \
        #    1 ___ 2
        #           \
        #           3 __ 5
        #
        # Three critical places: 1, 2, 3
        self.assertEqual(3, critical_place_count(network))


if __name__ == "__main__":
    unittest.main(verbosity=2)

