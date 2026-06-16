from collections import OrderedDict


class LFUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.frequency = 1


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_frequency = 0
        self.cache = {}               
        self.freq_map = {}            


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._update_node(node)

        return node.value


    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._update_node(node)

        else:
            if len(self.cache) >= self.capacity:

                min_list = self.freq_map[self.min_frequency]
                remove_key, _ = min_list.popitem(last=False)
                del self.cache[remove_key]
                if not min_list:
                    del self.freq_map[self.min_frequency]


            node = self.Node(key, value)
            self.cache[key] = node
            self.min_frequency = 1

            if 1 not in self.freq_map:
                self.freq_map[1] = OrderedDict()

            self.freq_map[1][key] = node


    def _update_node(self, node):
        old_frequency = node.frequency

        del self.freq_map[old_frequency][node.key]


        if len(self.freq_map[old_frequency]) == 0:
            del self.freq_map[old_frequency]

            if self.min_frequency == old_frequency:
                self.min_frequency += 1

        node.frequency += 1

        if node.frequency not in self.freq_map:
            self.freq_map[node.frequency] = OrderedDict()

        self.freq_map[node.frequency][node.key] = node


import unittest


class TestLFUCache(unittest.TestCase):

    def setUp(self):
        self.cache = LFUCache(2)


    def test_basic_put_and_get(self):
        self.cache.put(1, 100)
        self.cache.put(2, 200)

        self.assertEqual(self.cache.get(1), 100)
        self.assertEqual(self.cache.get(2), 200)


    def test_missing_key_returns_minus_one(self):
        self.assertEqual(self.cache.get(999), -1)


    def test_lfu_eviction(self):
        cache = LFUCache(2)

        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(3, 3)

        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)


    def test_lru_eviction_when_same_frequency(self):
        cache = LFUCache(2)

        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)

        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)


    def test_update_existing_key(self):
        cache = LFUCache(2)

        cache.put(1, 10)
        cache.put(1, 20)

        self.assertEqual(cache.get(1), 20)


    def test_frequency_changes_after_get(self):
        cache = LFUCache(2)

        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(3, 3)

        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)


    def test_capacity_zero(self):
        cache = LFUCache(0)
        cache.put(1, 1)
        self.assertEqual(cache.get(1), -1)



if __name__ == "__main__":
    unittest.main()