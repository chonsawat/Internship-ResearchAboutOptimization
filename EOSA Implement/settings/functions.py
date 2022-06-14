import numpy as np


def cost_function(X: np.array) -> float:
    return sum(X ** 2)
