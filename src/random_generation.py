"""
Python script file containing functions for random generation.
"""


import random


def random_function(num):
    """
    random_function returns a num long list of random values
    """
    random_list=[]
    for _ in range(num):
        random_list.append(random.random())
    return random_list
