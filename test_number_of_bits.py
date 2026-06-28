import unittest


class Binary:

    @staticmethod
    def number_of_bits(num):
         counter = 0
         while num>0:
             a = num & 1
             if a == 1:
                counter += 1
             num = num >> 1
         return counter





class TestNumberOfBits(unittest.TestCase):

    def test_example_eleven(self):
        """Test our favorite number 11 (binary 1011) -> should have 3 set bits"""
        self.assertEqual(Binary.number_of_bits(11), 3)

    def test_example_twelve(self):
        """Test number 12 (binary 1100) -> should have 2 set bits"""
        self.assertEqual(Binary.number_of_bits(12), 2)

    def test_zero_edge_case(self):
        """Test the absolute boundary case 0 -> should have 0 set bits"""
        self.assertEqual(Binary.number_of_bits(0), 0)

    def test_single_bit(self):
        """Test a pure power of 2 like 16 (binary 10000) -> should have exactly 1 set bit"""
        self.assertEqual(Binary.number_of_bits(16), 1)

    def test_large_number(self):
        """Test a larger number like 125 (binary 1111101) -> should have 6 set bits"""
        self.assertEqual(Binary.number_of_bits(125), 6)

# This line lets you execute the test file directly from your terminal
if __name__ == '__main__':
    unittest.main()
