import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from text_vectorization import train_tokenizer, random_vectorized_sample, stack_samples
from utils import get_dataset_dimensions

# Load the preprocessed data

df = pd.read_csv('./data/data/customer_support_tickets_preprocessed.csv')
X = df['Ticket Description']
y = df['Ticket Subject']

# Split the data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

train_sentences = X_train.tolist()
test_sentences = X_test.tolist()

# Create the tokenizer

MAX_TOKENS = 65000
OUTPUT_SEQ_LEN = 500

vectorizer = train_tokenizer(train_sentences, MAX_TOKENS, OUTPUT_SEQ_LEN)
#random_vectorized_sample(test_sentences, vectorizer)

# Reconstruct the data 

X_train_final = stack_samples(train_sentences, vectorizer)
X_test_final = stack_samples(test_sentences, vectorizer)
y_train_final = np.expand_dims(y_train, axis = 1).T
y_test_final = np.expand_dims(y_test, axis = 1).T

# Get the dimension for the training part

m, nx, ny = get_dataset_dimensions(X_train_final, y_train_final)
print(f"Number of training samples: {m}\n")
print(f"Number of input features: {nx}\n")
print(f"Number of output labels: {ny}\n")