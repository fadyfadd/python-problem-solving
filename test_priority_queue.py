import unittest


class PriorityQueue:
 
    def __init__(self):
        self._heap = []
 
    def count(self):
        return len(self._heap)
 
    def enqueue(self, element, priority):
        self._heap.append({"element": element, "priority": priority})
        self._heapify_up(len(self._heap) - 1)
 
    def dequeue(self):
        if len(self._heap) == 0:
            raise IndexError("The queue is empty.")
 
        root_element = self._heap[0]["element"]
        last_index = len(self._heap) - 1
 
        self._heap[0] = self._heap[last_index]
        self._heap.pop()
 
        if len(self._heap) > 0:
            self._heapify_down(0)
 
        return root_element
 
    def peek(self):
        if len(self._heap) == 0:
            raise IndexError("The queue is empty.")
        return self._heap[0]["element"]
 
    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
 
            if self._heap[index]["priority"] >= self._heap[parent_index]["priority"]:
                break
 
            self._swap(index, parent_index)
            index = parent_index
 
    def _heapify_down(self, index):
        last_index = len(self._heap) - 1
 
        while True:
            left_child = (2 * index) + 1
            right_child = (2 * index) + 2
            smallest = index
 
            if left_child <= last_index and self._heap[left_child]["priority"] < self._heap[smallest]["priority"]:
                smallest = left_child
 
            if right_child <= last_index and self._heap[right_child]["priority"] < self._heap[smallest]["priority"]:
                smallest = right_child
 
            if smallest == index:
                break
 
            self._swap(index, smallest)
            index = smallest
 
    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]


class UnitTests(unittest.TestCase):

    def setUp(self):
        """Provides a fresh, empty PriorityQueue instance before each test."""
        self.pq = PriorityQueue()

    def test_basic_operations(self):
        """Standard case: Items should be enqueued and dequeued in priority order."""
        self.pq.enqueue("task_low", 3)
        self.pq.enqueue("task_high", 1)
        self.pq.enqueue("task_mid", 2)

        self.assertEqual(self.pq.dequeue(), "task_high")
        self.assertEqual(self.pq.dequeue(), "task_mid")
        self.assertEqual(self.pq.dequeue(), "task_low")

    def test_peek(self):
        """State check: peeking should look at the top item without removing it."""
        self.pq.enqueue("clean_room", 2)
        self.pq.enqueue("do_homework", 1)
        self.assertEqual(self.pq.peek(), "do_homework")
        self.assertEqual(self.pq.peek(), "do_homework")

    def test_empty_and_size(self):
        """Utility check: verifies size changes and empty boundary flags."""
        self.assertEqual(self.pq.count(), 0)
        self.pq.enqueue("coffee_break", 1)
        self.assertGreater(self.pq.count(), 0)
        self.assertEqual(self.pq.count(), 1)

    def test_dequeue_empty_exception(self):
        """Edge case: Dequeuing from an empty queue should raise an IndexError."""
        with self.assertRaises(IndexError):
            self.pq.dequeue()

    def test_peek_empty_exception(self):
        """Edge case: Peeking at an empty queue should raise an IndexError."""
        with self.assertRaises(IndexError):
            self.pq.peek()

    def test_duplicate_priorities_fifo(self):
        """Stability check: Items with identical priorities should retain order."""
        self.pq.enqueue("first_equal", 5)
        self.pq.enqueue("second_equal", 5)
        self.assertEqual(self.pq.dequeue(), "first_equal")
        self.assertEqual(self.pq.dequeue(), "second_equal")