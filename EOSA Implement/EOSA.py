import numpy as np

class EOSA_base:
    def __init__(self):
        """
        Initialize for Ebola Optimization Search Algorithms
        """
        self.S = []
        self.E = []
        self.I = []
        self.H = []
        self.R = []
        self.V = []
        self.Q = []

        self.sols = None

        self.LowerBound = 0
        self.UpperBound = 1

    def createSusceptibleIndvd(self, psize) -> np.array:
        self.S = self.LowerBound + np.random.rand(psize) * (self.UpperBound + self.LowerBound)
        return self.S

    def generatedIndexCase(self, S):
        pass