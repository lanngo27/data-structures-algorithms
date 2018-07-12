import unittest

from hunt import safe_gold


class TestHunt(unittest.TestCase):

    def _test_level(self, level, correct_answer):
        returned_answer = safe_gold(level)
        self.assertEqual(
            returned_answer,
            correct_answer,
            "Your function returned {} when the correct answer is {}."
            .format(returned_answer, correct_answer) + "\n\n" +
            "Your function was tested with this level:\n{}".format(level)
        )


    def _test_files(self, filenames):
        for filename in filenames:
            with open(filename) as test_file:
                correct_answer = int(test_file.readline().strip())
                level = ''.join(test_file.readlines())
            self._test_level(level, correct_answer)


    def test_small(self):
        """safe_gold returns correct values for small levels. (2p)"""
        filenames = (
            "testdata/small.txt",
            "testdata/small2.txt",
            "testdata/small3.txt",
            "testdata/gamble.txt"
        )
        self._test_files(filenames)


    def test_large(self):
        """safe_gold returns correct values for large levels. (4p)"""
        filenames = (
            "testdata/large.txt",
            "testdata/trapped.txt",
            "testdata/eldorado.txt"
        )
        self._test_files(filenames)


if __name__ == "__main__":
    unittest.main(verbosity=2)
