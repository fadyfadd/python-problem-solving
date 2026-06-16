import unittest

class Node:
    def __init__(self, value: int, left: 'Node' = None, right: 'Node' = None):
        self.value = value
        self.left = left
        self.right = right


class SymmetricTreeChecker:
    def is_symmetric(self, root: Node) -> bool:
        if root is None:
            return True
        return self._is_symmetric_tree(root.left, root.right)

    def _is_symmetric_tree(self, left: Node, right: Node) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.value != right.value:
            return False
            
        return (self._is_symmetric_tree(left.left, right.right) and 
                self._is_symmetric_tree(left.right, right.left))


class TestSymmetricTreeChecker(unittest.TestCase):
    def setUp(self):
        self.checker = SymmetricTreeChecker()

    def test_empty_tree_is_symmetric(self):
        self.assertTrue(self.checker.is_symmetric(None))

    def test_single_node_is_symmetric(self):
        root = Node(1)
        self.assertTrue(self.checker.is_symmetric(root))

    def test_perfect_symmetric_tree(self):
        root = Node(1,
            Node(2, Node(3), Node(4)),
            Node(2, Node(4), Node(3))
        )
        self.assertTrue(self.checker.is_symmetric(root))

    def test_asymmetric_values(self):
        root = Node(1,
            Node(2, None, Node(3)),
            Node(2, None, Node(4))
        )
        self.assertFalse(self.checker.is_symmetric(root))

    def test_asymmetric_structure(self):
        root = Node(1,
            Node(2, Node(3), None),
            Node(2, None, None)
        )
        self.assertFalse(self.checker.is_symmetric(root))

    def test_symmetric_outer_but_asymmetric_inner_values(self):
        root = Node(1,
            Node(2, Node(3), Node(4)),
            Node(2, Node(3), Node(4))
        )
        self.assertFalse(self.checker.is_symmetric(root))

if __name__ == '__main__':
    unittest.main()