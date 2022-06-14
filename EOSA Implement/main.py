"""
Implement Ebola Optimization Search Algorithms
    ref: https://ieeexplore.ieee.org/document/9698015


"""
# Import
import numpy as np
from numpy import random
from sklearn.datasets import load_iris
from settings.constants import (modelrates,
                                root_paras)

# TODO: Delete while finished
from pprint import pprint
import pyswarms as ps


""" Docstrings for Ebola Optimizations Search Algorithms

Ebola Optimization Search Algorithms Base Class Description:
    Variables description:

    Methods description:
        createSusceptibleIndvd:
        generatedIndexCase:

"""


class Root:
    def __init__(self, root_algo_paras=None):
        self.problem_size = root_algo_paras["problem_size"]
        self.domain_range = root_algo_paras["domain_range"]
        self.print_train = root_algo_paras["print_train"]
        self.objective_func = root_algo_paras["objective_func"]
        self.solution, self.loss_train = None, []

    def _create_solution__(self):
        solution = np.random.uniform(self.domain_range[0], self.domain_range[1], self.problem_size)
        fitness = self._fitness_model__
        return [solution, fitness]

    def _fitness_model__(self):
        """ Assumption that objective function always return the original value """
        return self.objective_func()


class EOSA_base(Root):
    def __init__(self, root_algo_paras=None, pop_size=None, modelrates=None):
        """
        Initialize for Ebola Optimization Search Algorithms
        """
        Root.__init__(self, root_algo_paras)
        self.S = self.E = self.I = self.H = self.R = self.V = self.Q = []
        self.s_epoch = self.i_epoch = self.h_epoch = self.r_epoch = self.v_epoch = self.d_epoch = self.q_epoch = []

        self.pop_size = pop_size
        self.modelrates = modelrates

        self.sols = None
        self.gbest = float('-inf')

    def createSusceptibleIndvd(self, LowerBound=0, UpperBound=1) -> np.array:
        self.S = [(i, self._create_solution__()) for i in range(self.pop_size)]

    def generatedIndexCase(self, S: np.array) -> tuple[float, float]:
        self.gbest = cbest = float('inf')
        return self.gbest, cbest


# Run
if __name__ == "__main__":
    # Set seed for always same random number generator
    np.random.seed(42)

    # Ebola Algorithms Object
    ebola_optimization_search_algorithms = EOSA_base(root_algo_paras=root_paras, pop_size=100, modelrates=modelrates)
    ebola_optimization_search_algorithms.createSusceptibleIndvd()
    pprint(ebola_optimization_search_algorithms.S)

