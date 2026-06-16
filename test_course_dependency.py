from collections import defaultdict
import unittest

class CourseDependencyChecker:
    def can_finish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)
            
        visited = set()
        path_stack = set()
        
        def is_cyclic(curr):
            if curr in path_stack:
                return True
            if curr in visited:
                return False
                
            path_stack.add(curr)
            
            for neighbor in adj[curr]:
                if is_cyclic(neighbor):
                    return True
                    
            path_stack.remove(curr)
            visited.add(curr)
            return False

        for i in range(num_courses):
            if is_cyclic(i):
                return False
        return True
    

 
class UnitTests(unittest.TestCase):
    def setUp(self):
        self.checker = CourseDependencyChecker()

    def test_no_prerequisites(self):
        self.assertTrue(self.checker.can_finish(3, []))

    def test_valid_linear_dependencies(self):
        prerequisites = [[1, 0], [2, 1]]
        self.assertTrue(self.checker.can_finish(3, prerequisites))

    def test_direct_cycle(self):
        prerequisites = [[1, 0], [0, 1]]
        self.assertFalse(self.checker.can_finish(2, prerequisites))

    def test_longer_cycle(self):
        prerequisites = [[1, 0], [2, 1], [0, 2]]
        self.assertFalse(self.checker.can_finish(3, prerequisites))

    def test_multiple_disconnected_components_valid(self):
        prerequisites = [[1, 0], [3, 2]]
        self.assertTrue(self.checker.can_finish(4, prerequisites))

    def test_multiple_components_with_one_cycle(self):
        prerequisites = [[1, 0], [3, 2], [2, 3]]
        self.assertFalse(self.checker.can_finish(4, prerequisites))

if __name__ == "__main__":
    unittest.main()