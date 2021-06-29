"""
Main running script for the project
"""


import numpy as np
from src.random_generation import random_function
from src import Polynomial

if __name__ == '__main__':
    coeffs = np.array([1,0,0])
    polynom = Polynomial(coeffs)
    print(polynom.evaluate(3))
    print(polynom.roots())
    print(random_function(10))
