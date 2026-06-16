import unittest
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class BstValidator:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        return self._validate(root, None, None)

    def _validate(self, node: Optional[TreeNode], min_val: Optional[int], max_val: Optional[int]) -> bool:
        if node is None:
            return True
        if (min_val is not None and node.val <= min_val) or (max_val is not None and node.val >= max_val):
            return False
        return self._validate(node.left, min_val, node.val) and self._validate(node.right, node.val, max_val)

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.validator = BstValidator()

    def test_empty_tree_is_valid(self):
        self.assertTrue(self.validator.is_valid_bst(None))

    def test_single_node_is_valid(self):
        self.assertTrue(self.validator.is_valid_bst(TreeNode(10)))

    def test_invalid_bst(self):
        root = TreeNode(5, TreeNode(1), TreeNode(4))
        self.assertFalse(self.validator.is_valid_bst(root))

    def test_invalid_bst_left_child(self):
        root = TreeNode(10, TreeNode(15), TreeNode(20))
        self.assertFalse(self.validator.is_valid_bst(root))

    def test_invalid_bst_sub_child(self):
        root = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))
        self.assertFalse(self.validator.is_valid_bst(root))

    def test_valid_bst_complex(self):
        root = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(12), TreeNode(20)))
        self.assertTrue(self.validator.is_valid_bst(root))

if __name__ == '__main__':
    unittest.main()