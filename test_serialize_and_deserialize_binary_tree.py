from collections import deque
from typing import Optional
import unittest

class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        self._serialize_helper(root, res)
        return "".join(res)

    def _serialize_helper(self, root: Optional[TreeNode], res: list) -> None:
        if root is None:
            res.append("#,")
            return
        res.append(f"{root.val},")
        self._serialize_helper(root.left, res)
        self._serialize_helper(root.right, res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        nodes = data.strip(",").split(",")
        queue = deque(nodes)
        return self._deserialize_helper(queue)

    def _deserialize_helper(self, queue: deque) -> Optional[TreeNode]:
        if not queue:
            return None
        current = queue.popleft()
        if current == "#":
            return None
        root = TreeNode(int(current))
        root.left = self._deserialize_helper(queue)
        root.right = self._deserialize_helper(queue)
        return root

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.codec = Codec()

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val and 
                self.is_same_tree(p.left, q.left) and 
                self.is_same_tree(p.right, q.right))

    def test_standard_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)

        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1,2,#,#,3,4,#,#,5,#,#,")

        deserialized = self.codec.deserialize(serialized)
        self.assertTrue(self.is_same_tree(root, deserialized))

    def test_empty_tree(self):
        root = None
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "#,")

        deserialized = self.codec.deserialize(serialized)
        self.assertIsNone(deserialized)

    def test_single_node(self):
        root = TreeNode(42)
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "42,#,#,")

        deserialized = self.codec.deserialize(serialized)
        self.assertTrue(self.is_same_tree(root, deserialized))

    def test_skewed_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)

        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1,2,3,#,#,#,#,")

        deserialized = self.codec.deserialize(serialized)
        self.assertTrue(self.is_same_tree(root, deserialized))

if __name__ == "__main__":
    unittest.main()