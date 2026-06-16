import unittest

class Compression:
    def encode(self, s: str) -> str:
        if not s:
            return s

        result = []
        count = 1
        n = len(s)

        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
            else:
                self._append_result(result, s[i - 1], count)
                count = 1                
         
        self._append_result(result, s[n - 1], count)
        return "".join(result)

    def _append_result(self, result: list, c: str, count: int) -> None:
        result.append(c)
        if count > 1:
            result.append(f"({count})")
 
class UnitTests(unittest.TestCase):
    def setUp(self):
        self.compressor = Compression()

    def test_empty_string(self):
        self.assertEqual(self.compressor.encode(""), "")

    def test_single_characters(self):
        self.assertEqual(self.compressor.encode("abcd"), "abcd")

    def test_repeated_characters(self):
        self.assertEqual(self.compressor.encode("aaabccdddd"), "a(3)bc(2)d(4)")

    def test_all_same_characters(self):
        self.assertEqual(self.compressor.encode("aaaa"), "a(4)")

    def test_single_character_string(self):
        self.assertEqual(self.compressor.encode("a"), "a")


if __name__ == "__main__":
    unittest.main()