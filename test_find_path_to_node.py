import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def find_path(self, node, target):
        if node is None:
            return None

        if node.value == target:
            return [node.value]
 
        path = self.find_path(node.left, target) or self.find_path(node.right, target)

        if path is not None:
            path.append(node.value)
            return path

        return None    

 
class UnitTests(unittest.TestCase):

    def setUp(self):
        """Sets up a sample tree before each test."""
        self.tree = BinaryTree()
        self.tree.root = Node(10)
        self.tree.root.left = Node(5)
        self.tree.root.right = Node(15)
        self.tree.root.left.left = Node(3)
        self.tree.root.left.right = Node(7)

    def test_find_root_path(self):
        """Should return just the root value when target is the root."""
        result = self.tree.find_path(self.tree.root, 10)
        self.assertEqual(result, [10])

    def test_find_leaf_path(self):
        """Should return the path from leaf to root (reversed order)."""
        result = self.tree.find_path(self.tree.root, 7)
         
        self.assertEqual(result, [7, 5, 10])

    def test_target_not_in_tree(self):
        """Should return None if the target value doesn't exist."""
        result = self.tree.find_path(self.tree.root, 99)
        self.assertIsNone(result)

    def test_empty_tree(self):
        """Should return None if the tree has no nodes."""
        empty_tree = BinaryTree()
        result = empty_tree.find_path(empty_tree.root, 10)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()