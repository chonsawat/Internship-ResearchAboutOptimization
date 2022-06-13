"""
Implement Ebola Optimization Search Algorithms

"""

# Import
from EOSA import EOSA_base
from settings.imports import *
from settings.constants import modelrates

# Run
if __name__ == "__main__":
    # Set seed for always same random number generator
    np.random.seed(42)

    # Constant Variables
    print(modelrates)

    # EBOA Object
    ebola_optimization_search_algorithms = EOSA_base()
    S = ebola_optimization_search_algorithms.createSusceptibleIndvd(100)
    icase = ebola_optimization_search_algorithms.generatedIndexCase(S)
    print(icase)
