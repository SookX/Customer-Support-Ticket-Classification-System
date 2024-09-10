import numpy as np

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
