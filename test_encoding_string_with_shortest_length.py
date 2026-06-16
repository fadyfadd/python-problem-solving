import unittest


class EncodeString:
    def encode(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
            
        dp = [["" for _ in range(n)] for _ in range(n)]
        
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                substr = s[i:j + 1]
                dp[i][j] = substr
                
                for k in range(i, j):
                    left = dp[i][k]
                    right = dp[k + 1][j]
                    if len(left) + len(right) < len(dp[i][j]):
                        dp[i][j] = left + right
                
                substr_len = len(substr)
                for k in range(1, (substr_len // 2) + 1):
                    if substr_len % k == 0:
                        pattern = substr[:k]
                        repeat = substr_len // k
                        if pattern * repeat == substr:
                            candidate = f"{dp[i][i + k - 1]}({repeat})"
                            if len(candidate) <= len(dp[i][j]):
                                dp[i][j] = candidate
                                
        return dp[0][n - 1]
   

 
class TestEncodeString(unittest.TestCase):
    def setUp(self):
        self.encoder = EncodeString()

    def test_empty_string(self):
        self.assertEqual(self.encoder.encode(""), "")

    def test_single_character(self):
        self.assertEqual(self.encoder.encode("a"), "a")

    def test_no_compression_needed(self):
        self.assertEqual(self.encoder.encode("abcdefg"), "abcdefg")

    def test_simple_repeated_pattern(self):
        self.assertEqual(self.encoder.encode("aaaaa"), "a(5)")

    def test_complex_repeated_pattern(self):
        self.assertEqual(self.encoder.encode("abababab"), "ab(4)")

    def test_nested_or_partial_patterns(self):
        self.assertEqual(self.encoder.encode("aabcaabcaabc"), "aabc(3)")

    def test_shortest_encoding_decision(self):
        self.assertIn(self.encoder.encode("abababab"), ["ab(4)", "abababab"])


if __name__ == "__main__":
    unittest.main()   