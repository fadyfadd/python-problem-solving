import unittest


class StringUtilities:
    def longest_cons_string(self, input_str: str) -> str:
        dic = {}
        start = 0
        longest_string = ""
        
        for end in range(len(input_str)):
            c = input_str[end]
            
            if c in dic and dic[c] >= start:
                start = dic[c] + 1
                
            dic[c] = end
            
            current_string = input_str[start : end + 1]
            
            if len(current_string) > len(longest_string):
                longest_string = current_string
                
        return longest_string
    



class UnitTests(unittest.TestCase):

    def setUp(self):
        self.utils = StringUtilities()

    def test_standard_case(self):
        self.assertEqual(self.utils.longest_cons_string("abcabcbb"), "abc")

    def test_all_unique_characters(self):
        self.assertEqual(self.utils.longest_cons_string("abcdef"), "abcdef")

    def test_all_identical_characters(self):
        self.assertEqual(self.utils.longest_cons_string("bbbbb"), "b")

    def test_empty_string(self):
        self.assertEqual(self.utils.longest_cons_string(""), "")

    def test_single_character(self):
        self.assertEqual(self.utils.longest_cons_string("a"), "a")

    def test_substring_at_the_end(self):
        self.assertEqual(self.utils.longest_cons_string("pwwkew"), "wke")

    def test_characters_outside_current_window(self):
        self.assertEqual(self.utils.longest_cons_string("abba"), "ab")


if __name__ == "__main__":
    unittest.main()