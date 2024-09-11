import numpy as np
from utils import initialize_parameters, forward_propagation, sparse_categorical_crossentropy, backward_propagation, update_parameters

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

        
        self.parameters = initialize_parameters(layers_dim)
        parameters = self.parameters

        for epoch in range(epochs):

            print(f"\nEpoch: {epoch}")
            
            yhat, cache = forward_propagation(X, parameters)

            grads = backward_propagation(yhat, y, cache, parameters)
            
            parameters = update_parameters(parameters, grads, learning_rate)
        
        print(parameters['W1'])

    
    def predict(self, X):
       parameters = self.parameters
       
       yhat, _ = forward_propagation(X, parameters)
       
       predictions = np.argmax(yhat, axis=0)
       
       return predictions

    def load_weights(self, parameters):
        self.parameters = parameters
