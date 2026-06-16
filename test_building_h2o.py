import threading
import unittest

class ThreadedH2OSynthesizer:
    def __init__(self):
        self._sem_h = threading.Semaphore(2)
        self._sem_o = threading.Semaphore(1)        
        self._barrier = threading.Barrier(3)

    def hydrogen(self) -> None:
        self._sem_h.acquire()
        self._barrier.wait()
        print("H", end="", flush=True)
        self._sem_h.release()

    def oxygen(self) -> None:
        self._sem_o.acquire()
        self._barrier.wait()
        print("O", end="", flush=True)
        self._sem_o.release()



class UnitTests(unittest.TestCase):

    def test_single_molecule_synthesis(self):
        synthesizer = ThreadedH2OSynthesizer()

        output = []
        lock = threading.Lock()

        def hydrogen_worker():
            synthesizer.hydrogen()
            with lock:
                output.append("H")

        def oxygen_worker():
            synthesizer.oxygen()
            with lock:
                output.append("O")


        h1 = threading.Thread(target=hydrogen_worker)
        h2 = threading.Thread(target=hydrogen_worker)
        o1 = threading.Thread(target=oxygen_worker)

        o1.start()
        h2.start()
        h1.start()

        h1.join(timeout=2)
        h2.join(timeout=2)
        o1.join(timeout=2)

        self.assertFalse(h1.is_alive())
        self.assertFalse(h2.is_alive())
        self.assertFalse(o1.is_alive())

        print(f"\n[Basic Test] Resulting elements: {output}")

        self.assertEqual(len(output), 3)
        self.assertEqual(output.count("H"), 2)
        self.assertEqual(output.count("O"), 1)


if __name__ == "__main__":
    unittest.main()