import unittest


class DigitRotator:
    @staticmethod
    def rotate_right(n: int, k: int) -> int:
        digits = len(str(n))
        k %= digits

        if k == 0:
            return n

        power = 10 ** k

        right = n % power
        left = n // power

        return right * (10 ** (digits - k)) + left


class UnitTests(unittest.TestCase):

    def test_rotate_two_digits(self):
        self.assertEqual(
            DigitRotator.rotate_right(12345, 2),
            45123
        )

    def test_rotate_one_digit(self):
        self.assertEqual(
            DigitRotator.rotate_right(12345, 1),
            51234
        )

    def test_rotate_zero_digits(self):
        self.assertEqual(
            DigitRotator.rotate_right(12345, 0),
            12345
        )

    def test_rotate_by_length(self):
        self.assertEqual(
            DigitRotator.rotate_right(12345, 5),
            12345
        )

    def test_rotate_more_than_length(self):
        self.assertEqual(
            DigitRotator.rotate_right(12345, 7),
            45123
        )

