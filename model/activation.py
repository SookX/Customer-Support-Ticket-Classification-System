import numpy as np
from scipy.special import softmax

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x):
    return max(0.1 * x, x)

