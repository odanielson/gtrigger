"""Copyright 2014 odanielson@github.com, MIT-license"""

import unittest
import time

from gevent import sleep
from gevent.queue import Queue, Empty

from gtrigger.gtrigger import GTrigger

class TestGTrigger(unittest.TestCase):

    def test_trigger_interval(self):
        """Verify that trigger sends timestamp at queue on the right
        interval."""
        test_time = 0.2
        interval = 0.01
        trigger_queue = Queue()
        trigger = GTrigger(trigger_queue, interval)
        trigger.start()
        sleep(test_time)

        count = 0
        try:
            while True:
                trigger_queue.get(block=False)
                count += 1
        except Empty:
            pass
        expected = test_time / interval
        self.assertTrue(count >= expected -1 and count <= expected + 1)

if __name__ == '__main__':
    unittest.main()
