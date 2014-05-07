"""Copyright 2014 odanielson@github.com, MIT-license"""

import time

from gevent import spawn, sleep
from gevent.queue import Queue

from regulator import Regulator

class GTrigger(object):
    """Gtrigger implements a simple trigger for GEvent that sends an epoch
    timestamp on a Queue at a given interval.
    """
    def __init__(self, trigger_queue, interval=1.0, converge_factor=1.1):
        """GTrigger constructor

        Args -
        Queue trigger_queue - Queue to sent epoch timestamps on
        float interval - interval in seconds between each timestamp
        float converge_factor - factor controlling calibration speed
        """
        self.trigger_queue = trigger_queue
        self.delay = interval
        self.regulator = Regulator(interval, converge_factor)
        self.dispatch_greenlet = spawn(self._dispatch_loop)

    def start(self):
        """Start trigger."""
        self.dispatch_greenlet.start()

    def _dispatch_loop(self):

        old_t = None
        while True:

            t = time.time()
            if old_t:
                dt = t - old_t
                self.delay = self.regulator.sample(dt)

            old_t = t
            self.trigger_queue.put(t)
            sleep(self.delay)
