import threading
import time
from io import StringIO
import contextlib
import unittest
 
import threading

class PrintInOrder:
    def __init__(self):
        self.sem1 = threading.Semaphore(1)  
        self.sem2 = threading.Semaphore(0)  
        self.sem3 = threading.Semaphore(0) 

    def first(self, printFirst):
        self.sem1.acquire()
        printFirst()
        self.sem2.release()

    def second(self, printSecond):
        self.sem2.acquire()
        printSecond()
        self.sem3.release()

    def third(self, printThird):
        self.sem3.acquire()
        printThird()

 

class UnitTests(unittest.TestCase):

    def test_sequential_execution(self):
        engine = PrintInOrder()
        execution_order = []

        def printFirst():
            execution_order.append("First")

        def printSecond():
            execution_order.append("Second")

        def printThird():
            execution_order.append("Third")

        t1 = threading.Thread(target=engine.first, args=(printFirst,))
        t2 = threading.Thread(target=engine.second, args=(printSecond,))
        t3 = threading.Thread(target=engine.third, args=(printThird,))

        t3.start()
        t2.start()
        t1.start()

        t1.join()
        t2.join()
        t3.join()

        print(f"\n[Test Output] Order of execution: {execution_order}")
        self.assertEqual(execution_order, ["First", "Second", "Third"])