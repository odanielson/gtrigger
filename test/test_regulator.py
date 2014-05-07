"""Copyright 2014 odanielson@github.com, MIT-license"""

import unittest
import time

from gtrigger.regulator import Regulator

class TestRegulator(unittest.TestCase):

    def test_regulator_calibration(self):
        """Verify that the regulator adjusts the calibration factor."""
        interval = 0.01
        converge_factor = 0.1
        regulator = Regulator(interval, converge_factor=converge_factor)
        error = 0.01
        output = regulator.sample(interval + error)
        self.assertEquals(output, interval - (error * converge_factor))
        output = regulator.sample(interval + error)
        self.assertEquals(output, interval - (2 * error * converge_factor))

if __name__ == '__main__':
    unittest.main()
