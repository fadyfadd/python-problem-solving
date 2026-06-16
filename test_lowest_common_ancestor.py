import unittest

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def lowest_common_ancestor(self, root: Node, p: Node, q: Node) -> Node:
        if root is None or root == p or root == q:
            return root
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        return left if left is not None else right

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()
        self.tree.root = Node(3)
        self.tree.root.left = Node(5)
        self.tree.root.left.left = Node(6)
        self.tree.root.left.right = Node(2)
        self.tree.root.left.right.left = Node(7)
        self.tree.root.left.right.right = Node(4)
        self.tree.root.right = Node(1)
        self.tree.root.right.left = Node(0)
        self.tree.root.right.right = Node(8)
        
        self.node_3 = self.tree.root
        self.node_5 = self.tree.root.left
        self.node_1 = self.tree.root.right
        self.node_2 = self.tree.root.left.right
        self.node_4 = self.tree.root.left.right.right
        self.node_7 = self.tree.root.left.right.left
        self.node_8 = self.tree.root.right.right

    def test_lca_different_subtrees(self):
        result = self.tree.lowest_common_ancestor(self.tree.root, self.node_5, self.node_1)
        self.assertEqual(result, self.node_3)

    def test_lca_one_node_is_ancestor(self):
        result = self.tree.lowest_common_ancestor(self.tree.root, self.node_5, self.node_4)
        self.assertEqual(result, self.node_5)

    def test_lca_same_parent_subtrees(self):
        result = self.tree.lowest_common_ancestor(self.tree.root, self.node_7, self.node_4)
        self.assertEqual(result, self.node_2)

    def test_lca_root_and_leaf(self):
        result = self.tree.lowest_common_ancestor(self.tree.root, self.node_3, self.node_8)
        self.assertEqual(result, self.node_3)

if __name__ == '__main__':
    unittest.main()