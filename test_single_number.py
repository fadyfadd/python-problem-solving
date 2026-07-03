import unittest


class SingleNumberFinder:
    def find_single(self, nums: list[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result


class TestSingleNumberFinder(unittest.TestCase):

    def setUp(self):
        self.finder = SingleNumberFinder()

    def test_simple_case(self):
        self.assertEqual(
            self.finder.find_single([2, 2, 1]),
            1
        )

    def test_medium_case(self):
        self.assertEqual(
            self.finder.find_single([4, 1, 2, 1, 2]),
            4
        )

    def test_single_element(self):
        self.assertEqual(
            self.finder.find_single([99]),
            99
        )

    def test_negative_numbers(self):
        self.assertEqual(
            self.finder.find_single([-1, 5, 5]),
            -1
        )


if __name__ == "__main__":
    unittest.main()