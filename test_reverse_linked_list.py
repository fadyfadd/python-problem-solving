 
import unittest

class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

class LinkedListUtilities:
    def reverse(self, head):
        previous = None
        current = head
        
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            
        return previous


 
class UnitTests(unittest.TestCase):
    
    def setUp(self):
        self.utils = LinkedListUtilities()

    def _to_linked_list(self, elements):
        """Helper to create a linked list from a Python list."""
        if not elements:
            return None
        head = ListNode(elements[0])
        current = head
        for val in elements[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def _to_python_list(self, head):
        """Helper to convert a linked list back into a Python list for assertion."""
        elements = []
        current = head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    def test_reverse_multi_node_list(self):
         head = self._to_linked_list([1, 2, 3, 4])        
         reversed_head = self.utils.reverse(head)        
         self.assertEqual(self._to_python_list(reversed_head), [4, 3, 2, 1])

    def test_reverse_single_node_list(self):
        head = self._to_linked_list([42])   
        reversed_head = self.utils.reverse(head)
        self.assertEqual(self._to_python_list(reversed_head), [42])

    def test_reverse_empty_list(self):
        # Arrange: None
        head = None
        reversed_head = self.utils.reverse(head)
        self.assertIsNone(reversed_head)

    def test_reverse_two_nodes(self):
         head = self._to_linked_list([1, 2])        
         reversed_head = self.utils.reverse(head)        
         self.assertEqual(self._to_python_list(reversed_head), [2, 1])



if __name__ == '__main__':
    unittest.main()