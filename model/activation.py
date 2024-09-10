import numpy as np

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x):
    return max(0.1 * x, x)


