import unittest
 

class MatrixServices:
    def __init__(self):
        pass # Clean Pythonic empty initializer

    def mutliply(self, matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
        if len(matrix_a[0]) != len(matrix_b):
            raise ValueError("Number of columns in matrix A must be equal to number of rows in matrix B")
        
        result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
        
        for i in range(len(matrix_a)):
            for j in range(len(matrix_b[0])):
                for k in range(len(matrix_b)):
                    result[i][j] += matrix_a[i][k] * matrix_b[k][j]
        
        return result 
         

class UnitTests(unittest.TestCase):
    def setUp(self):
        """Initializes the MatrixServices instance before each test."""
        self.matrix_tool = MatrixServices()

    def test_standard_multiplication(self):
        """Tests standard matrix multiplication with positive integers."""
        matrix_a = [
            [1, 2],
            [3, 4]
        ]
        matrix_b = [
            [5, 6],
            [7, 8]
        ]
        expected = [
            [19, 22],
            [43, 50]
        ]
        self.assertEqual(self.matrix_tool.mutliply(matrix_a, matrix_b), expected)

    def test_non_square_matrices(self):
        """Tests multiplication of matrices with non-square dimensions (2x3 * 3x2)."""
        matrix_a = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        matrix_b = [
            [7, 8],
            [9, 1],
            [2, 3]
        ]
        expected = [
            [31, 19],
            [85, 55]
        ]
        self.assertEqual(self.matrix_tool.mutliply(matrix_a, matrix_b), expected)

    def test_identity_matrix(self):
        """Tests that multiplying by an identity matrix returns the original matrix."""
        matrix_a = [
            [1, 2],
            [3, 4]
        ]
        identity_matrix = [
            [1, 0],
            [0, 1]
        ]
        self.assertEqual(self.matrix_tool.mutliply(matrix_a, identity_matrix), matrix_a)

    def test_negative_numbers_and_zeros(self):
        """Tests multiplication involving negative numbers and zeros."""
        matrix_a = [
            [0, -2],
            [3, 5]
        ]
        matrix_b = [
            [4, 1],
            [-1, 0]
        ]
        expected = [
            [2, 0],
            [7, 3]
        ]
        self.assertEqual(self.matrix_tool.mutliply(matrix_a, matrix_b), expected)

    def test_incompatible_dimensions_raises_error(self):
        """Tests that a ValueError is raised when dimensions are incompatible."""
        matrix_a = [
            [1, 2, 3], # Fixed comment: 3 columns
            [4, 5, 6]
        ]
        matrix_b = [
            [1, 2]     # 1 row
        ]
        
        with self.assertRaises(ValueError) as context:
            self.matrix_tool.mutliply(matrix_a, matrix_b)
            
        self.assertEqual(
            str(context.exception), 
            "Number of columns in matrix A must be equal to number of rows in matrix B"
        )

if __name__ == '__main__':
    unittest.main()