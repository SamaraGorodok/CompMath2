def der(func,h=0.000000001):
    return lambda x: (func(x+h) - func(x-h)) / (2*h)