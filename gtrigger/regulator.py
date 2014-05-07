"""Copyright 2014 odanielson@github.com, MIT-license"""


class Regulator(object):
    """Regulator implements a very simple regulator
    where the output is the setpoint + a calibration value
    determined from

    calibration -= error * converge_factor_factor
    """

    def __init__(self, setpoint=1.0, converge_factor=0.1):
        self.setpoint = setpoint
        self.converge_factor = converge_factor
        self.calibration = 0.0

    def sample(self, value):

        error = value - self.setpoint
        self.calibration -= error * self.converge_factor
        return self.setpoint + self.calibration
