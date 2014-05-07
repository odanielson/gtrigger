#!/usr/bin/python
"""Copyright 2014 odanielson@github.com, MIT-license

Testtool to log trigger accuracy for a given interval.
"""

import sys

from gevent.queue import Queue

from gtrigger.gtrigger import GTrigger

if len(sys.argv) < 2:
    print "Usage: %s interval[s]"
    exit(1)


interval = float(sys.argv[1])
print "Test trigger accuracy for given interval %f" % interval

trigger_queue = Queue()
trigger = GTrigger(trigger_queue, interval=interval)
trigger.start()

old_t = None
dt_buffer = []
while True:
    t = trigger_queue.get()
    if old_t:
        dt = t - old_t
        dt_buffer.append(dt)
        if len(dt_buffer) > 100:
            dt_buffer.pop(0)
        mean = sum(dt_buffer) / len(dt_buffer)
        mean_error = interval - mean
        print "t=%f dt=%f mean dt=%f mean error=%f" % (t, dt, mean, mean_error)
    old_t = t
