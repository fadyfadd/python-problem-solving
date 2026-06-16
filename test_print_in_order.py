import threading
import time
from io import StringIO
import contextlib
import unittest
 
class PrintInOrder:
    def __init__(self):
        self.stage = 1
        self.condition = threading.Condition()
 
    def first(self, worker_thread):
        with self.condition:
            worker_thread.start()
            self.stage = 2
            self.condition.notify_all()
 
    def second(self, worker_thread):
        with self.condition:
            while self.stage != 2:
                self.condition.wait()
            worker_thread.start()
            self.stage = 3
            self.condition.notify_all()
 
    def third(self, worker_thread):
        with self.condition:
            while self.stage != 3:
                self.condition.wait()
            worker_thread.start()
 

    def test_sequential_execution(self):
        """Pass workers straight to engine via background invocations to avoid deadlocks."""
        engine = PrintInOrder()
        execution_order = []

        t1 = threading.Thread(target=lambda: execution_order.append("First"))
        t2 = threading.Thread(target=lambda: execution_order.append("Second"))
        t3 = threading.Thread(target=lambda: execution_order.append("Third"))
 
        call_third = threading.Thread(target=engine.third, args=(t3,))
        call_second = threading.Thread(target=engine.second, args=(t2,))
        
        call_third.start()   
        call_second.start()   
        time.sleep(0.05)      

        engine.first(t1)      
        call_third.join()
        call_second.join()
        
        t1.join()
        t2.join()
        t3.join()

        self.assertEqual(execution_order, ["First", "Second", "Third"])

if __name__ == "__main__":
    unittest.main()