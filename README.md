gtrigger
========

Status: Lab

Gtrigger implements a very simple trigger library for gevent.
It can be used to trigger messages on a Queue at regular intervals.

Usage
-----

    from gevent.queue import Queue
    from gtrigger.gtrigger import GTrigger

    trigger_queue = Queue()
    trigger = GTrigger(trigger_queue, 1.0)
    trigger.start()

    trigger_queue.get()


Accuracy
--------

You can test the raw accuracy by running a test tool for a given interval

    ./tools/testtool.py interval

Have in mind that the triggering accuracy will be heavily affected by other
running greenlets when used in a real application.


TODO
----

Consider other approaches for reaching a good mean value, for example
regulating on the mean value of a history buffer of intervals.
