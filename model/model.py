import numpy as np
from utils import initialize_parameters, forward_propagation, sparse_categorical_crossentropy
# layers_dims = [500, 10, 10, 16]
class MCC:
    def __init__(self, X, y, epochs, learning_rate, layers_dim):
        self.X = X
        self.y = y
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.layers_dim = layers_dim

    def fit(self):
        X = self.X
        y = self.y
        epochs = self.epochs
        learning_rate = self.learning_rate
        layers_dim = self.layers_dim
        parameters = initialize_parameters(layers_dim)
        yhat, cache = forward_propagation(X, parameters)
        cost = sparse_categorical_crossentropy(y, yhat)
        
        #for key, value in parameters.items():
        #    print(f"Weight {key} with size {value.shape}")