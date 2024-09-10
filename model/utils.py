import numpy as np
from activation import relu, softmax

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

    """
    Initialize the weight and bias parameters for a neural network.

    Parameters:
    - layer_dims: A list where each element represents the number of units in each layer of the neural network.
                  For example, layer_dims = [5, 4, 3] represents a network with:
                  - 5 units in the input layer,
                  - 4 units in the first hidden layer,
                  - 3 units in the output layer.

    Returns:
    - parameters: A dictionary containing the initialized weights and biases for each layer of the network.
                  The keys are:
                  - 'W1', 'W2', ..., 'WL-1' for the weight matrices,
                  - 'B1', 'B2', ..., 'BL-1' for the bias vectors.
    
    - W[l]: A weight matrix of shape (layer_dims[l], layer_dims[l-1]) initialized with random values.
            This matrix connects layer l-1 to layer l.
    - B[l]: A bias vector of shape (layer_dims[l], 1) initialized with zeros for the neurons in layer l.
    """
    
    parameters = {}

    L = len(layer_dims)

    for l in range(1, L):

        parameters['W' + str(l)] = np.random.rand(layer_dims[l], layer_dims[l - 1])
        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))

    return parameters


def forward_propagation(X, parameters):

    """
    Implements the forward propagation for a L-layer neural network.

    Parameters:
    - X: Input data of shape (num_features, num_samples).
    - parameters: Dictionary containing the parameters (weights and biases).

    Returns:
    - yhat: The output after applying softmax (predictions).
    - cache: A dictionary containing intermediate values (Z, A) for backward propagation.
    """

    L = len(parameters) // 2  # Number of layers (W, b pairs)

    cache = {}
    A_temp = X
    for l in range(1, L):
        Z = np.dot(parameters['W' + str(l)], A_temp) + parameters['b' + str(l)] 
        cache['Z' + str(l)] = Z
        A_temp = relu(Z)
        cache['A' + str(l)] = A_temp
    
    ZL = np.dot(parameters['W' + str(L)], A_temp) + parameters['b' + str(L)]
    cache['Z' + str(L)] = ZL
    
    yhat = softmax(ZL)
    print(yhat.dtype)
    return yhat, cache


def sparse_categorical_crossentropy(y_true, y_pred):

    y_true_onehot = np.zeros_like(y_pred)
    y_true_onehot[np.arange(len(y_true)), y_true] = 1

    # calculate loss
    loss = -np.mean(np.sum(y_true_onehot * np.log(y_pred), axis=-1))

    return loss