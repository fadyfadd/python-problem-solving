import threading
from typing import Callable
import unittest
import threading

class ThreadedH2OSynthesizer:
    def __init__(self):
        self._sem_h = threading.Semaphore(2)
        self._sem_o = threading.Semaphore(1)        
        self._barrier = threading.Barrier(3)

    def hydrogen(self, release_hydrogen: Callable[[], None]) -> None:
         with self._sem_h:
            release_hydrogen() 
            self._barrier.wait()

    def oxygen(self, release_oxygen: Callable[[], None]) -> None:
        with self._sem_o:
            release_oxygen() 
            self._barrier.wait()



class UnitTests(unittest.TestCase):
    
    def test_single_molecule_synthesis(self):
        synthesizer = ThreadedH2OSynthesizer()
        output = []
        lock = threading.Lock()
        
        def release_h():
            with lock:
                output.append("H")
                
        def release_o():
            with lock:
                output.append("O")

        h1 = threading.Thread(target=synthesizer.hydrogen, args=(release_h,))
        h2 = threading.Thread(target=synthesizer.hydrogen, args=(release_h,))
        o1 = threading.Thread(target=synthesizer.oxygen, args=(release_o,))

        h1.start()
        h2.start()
        o1.start()

        h1.join(timeout=2.0)
        h2.join(timeout=2.0)
        o1.join(timeout=2.0)

        if h1.is_alive() or h2.is_alive() or o1.is_alive():
            self.fail("The threads deadlocked and failed to pass the barrier!")

        print(f"\n[Basic Test] Resulting elements: {output}")
        self.assertEqual(len(output), 3, "Should have exactly 3 elements")
        self.assertEqual(output.count("H"), 2, "Should have exactly 2 Hydrogen")
        self.assertEqual(output.count("O"), 1, "Should have exactly 1 Oxygen")

if __name__ == "__main__":
    unittest.main()