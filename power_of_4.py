import unittest


class PowerOfFourChecker:
    def is_power_of_four(self, n: int) -> bool:
        if n <= 0:
            return False

        if (n & (n - 1)) != 0:
            return False

        pos = 0

        while n > 1:
            n >>= 1
            pos += 1

        return pos % 2 == 0


class TestPowerOfFourChecker(unittest.TestCase):

    def setUp(self):
        self.checker = PowerOfFourChecker()

    def test_valid_powers_of_four(self):
        self.assertTrue(self.checker.is_power_of_four(1))
        self.assertTrue(self.checker.is_power_of_four(4))
        self.assertTrue(self.checker.is_power_of_four(16))
        self.assertTrue(self.checker.is_power_of_four(64))
        self.assertTrue(self.checker.is_power_of_four(256))

    def test_invalid_values(self):
        self.assertFalse(self.checker.is_power_of_four(0))
        self.assertFalse(self.checker.is_power_of_four(-4))
        self.assertFalse(self.checker.is_power_of_four(2))
        self.assertFalse(self.checker.is_power_of_four(8))
        self.assertFalse(self.checker.is_power_of_four(32))
        self.assertFalse(self.checker.is_power_of_four(128))
        self.assertFalse(self.checker.is_power_of_four(5))
        self.assertFalse(self.checker.is_power_of_four(10))


if __name__ == "__main__":
    unittest.main()