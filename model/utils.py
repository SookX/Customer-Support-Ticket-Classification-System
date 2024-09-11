import numpy as np
from activation import relu
from scipy.special import softmax
from copy import deepcopy

def get_dataset_dimensions(features, labels):

    """
    Retrieve the dimensions of the feature and label datasets.

    Parameters:
    - features: A NumPy array or similar data structure containing the feature data with shape (num_samples, num_features).
    - labels: A NumPy array or similar data structure containing the label data with shape (num_samples, num_labels).

    Returns:
    - num_samples: The number of samples (rows) in the feature dataset.
    - num_features: The number of features (columns) in the feature dataset.
    - num_labels: The number of labels (columns) in the label dataset.
    """

    num_samples = features.shape[1]  # Number of samples
    num_features = features.shape[0]  # Number of features
    num_labels = labels.shape[0]     # Number of labels
    
    return num_samples, num_features, num_labels

def initialize_parameters(layer_dims):
    parameters = {}
    L = len(layer_dims)
    for l in range(1, L):
        parameters['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l - 1]) * np.sqrt(2 / layer_dims[l - 1])
        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))
    return parameters


def forward_propagation(X, parameters):
    L = len(parameters) // 2
    cache = {}
    A_temp = X
    for l in range(1, L):
        Z = np.dot(parameters['W' + str(l)], A_temp) + parameters['b' + str(l)] 
        cache['Z' + str(l)] = Z
        A_temp = relu(Z)
        cache['A' + str(l)] = A_temp
    
    ZL = np.dot(parameters['W' + str(L)], A_temp) + parameters['b' + str(L)]
    cache['Z' + str(L)] = ZL
    
    yhat = softmax(ZL, axis=1)
    cache['A0'] = X
    
    return yhat, cache

def sparse_categorical_crossentropy(y_true, y_pred):
    y_true_onehot = np.zeros_like(y_pred)
    y_true_onehot[np.arange(len(y_true)), y_true] = 1
    cost = -np.mean(np.sum(y_true_onehot * np.log(y_pred), axis=-1))
    return cost

def backward_propagation(yhat, Y, cache, parameters):
    grads = {}
    L = len(parameters) // 2  
    m = yhat.shape[1]         
    
    dZL = yhat - Y
    A_prev_L = cache['A' + str(L-1)]
    W_L = parameters['W' + str(L)]
    
    dW_L = (1/m) * np.dot(dZL, A_prev_L.T)
    db_L = (1/m) * np.sum(dZL, axis=1, keepdims=True)
    
    grads['dW' + str(L)] = dW_L
    grads['db' + str(L)] = db_L
    
    dA_prev = np.dot(W_L.T, dZL)
    
    for l in reversed(range(1, L)):
        A_prev = cache['A' + str(l-1)] if l > 1 else cache['A0']
        Z = cache['Z' + str(l)]
        
        dZ = np.multiply(dA_prev, np.where(Z > 0, 1, 0)) 
        
        
        dW = (1/m) * np.dot(dZ, A_prev.T)
        db = (1/m) * np.sum(dZ, axis=1, keepdims=True)
        
        grads['dW' + str(l)] = dW
        grads['db' + str(l)] = db
        
    print("Gradients:", grads)  
    return grads



def update_parameters(parameters, grads, learning_rate):
    parameters = deepcopy(parameters)
    L = len(parameters) // 2
    for l in range(1, L + 1):
        parameters['W' + str(l)] -= learning_rate * grads['dW' + str(l)]
        parameters['b' + str(l)] -= learning_rate * grads['db' + str(l)]
    return parameters