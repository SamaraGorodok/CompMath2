import numpy as np
from numpy import sin


def get_function(num):
    if (num == 1):
        return np.linspace(-5, 5, 200), lambda x: 2.3 * x ** 3 + 5 * (x ** 2) - 7.41 * x - 10.6
    if (num == 2):
        return np.linspace(-5, 5, 200), lambda x: x ** 2 + 50 + 24 * x
    if (num == 3):
        return np.linspace(-10, 10, 200), lambda x: 4.3*np.cos(x) + np.cos(x) - 5

def get_system(num):
    if (num==1):
        return np.linspace(-5,5,200), lambda x, y : x**2 + y**2 - 4
    if (num==2):
        return np.linspace(-5,5,200), lambda x, y : x**3 + y - 1
    if (num ==3):
        return np.linspace(-5, 5, 200), lambda x, y: x**2 - y - 3
