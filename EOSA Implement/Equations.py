"""
This module used for solving the equations to EOSA.py Module
"""


import numpy as np


def equation_4(individual_lower_bound, individual_upper_bound):
    return individual_lower_bound + np.random.rand() * (individual_upper_bound + individual_lower_bound)
