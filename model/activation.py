import numpy as np

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x):
    return max(0.1 * x, x)

def softmax(z, epsilon=1e-12):

    z_exp = np.exp(z - np.max(z, axis=0, keepdims=True))
    
    sum_z_exp = np.sum(z_exp, axis=0, keepdims=True) 
    
    return z_exp / (sum_z_exp + epsilon)  
