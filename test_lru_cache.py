class LRUCache:

    class Node:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.head = self.Node()
        self.tail = self.Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])

        if len(self.map) == self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]

        node = self.Node(key, value)
        self._insert(node)
        self.map[key] = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head



import unittest



class UnitTests(unittest.TestCase):

    def test_basic_put_get(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)

        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)

    def test_eviction_lru(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)

        # 1 becomes LRU after accessing 2
        cache.put(3, 3)  # evicts key 1

        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(1, 10)

        self.assertEqual(cache.get(1), 10)

    def test_lru_order_changes_on_get(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)

        cache.get(1)        
        cache.put(3, 3)     

        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(3), 3)

    def test_capacity_one(self):
        cache = LRUCache(1)
        cache.put(1, 1)
        cache.put(2, 2)

        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)

    def test_get_nonexistent(self):
        cache = LRUCache(2)
        self.assertEqual(cache.get(99), -1)


if __name__ == "__main__":
    unittest.main()