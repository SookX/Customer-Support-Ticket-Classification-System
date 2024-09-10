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

        # Initialize model parameters
        self.parameters = initialize_parameters(layers_dim)
        parameters = self.parameters

        # Perform forward propagation
        yhat, cache = forward_propagation(X, parameters)

        # Compute the cost using sparse categorical cross-entropy
        cost = sparse_categorical_crossentropy(y, yhat)

    
    def predict(self, X):
       parameters = self.parameters
       
       # Perform forward propagation to get predictions
       yhat, _ = forward_propagation(X, parameters)
       
       # Get the predicted class with the highest probability for each sample
       predictions = np.argmax(yhat, axis=0)
       
       return predictions

    def load_weights(self, parameters):
        self.parameters = parameters
