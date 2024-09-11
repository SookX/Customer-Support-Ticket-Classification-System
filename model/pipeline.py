import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from text_vectorization import train_tokenizer, random_vectorized_sample, stack_samples
from utils import get_dataset_dimensions
from model import MCC

# Load the preprocessed data

df = pd.read_csv('./data/data/customer_support_tickets_preprocessed.csv')
X = df['Ticket Description']
y = df['Ticket Subject']

categories = y.unique()
category_to_num = {category: idx for idx, category in enumerate(categories)}

y_encoded = y.map(category_to_num)
# Split the data

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size = 0.2)

train_sentences = X_train.tolist()
test_sentences = X_test.tolist()

# Create the tokenizer


MAX_TOKENS = 65000
OUTPUT_SEQ_LEN = 500

vectorizer = train_tokenizer(train_sentences, MAX_TOKENS, OUTPUT_SEQ_LEN)
#random_vectorized_sample(test_sentences, vectorizer)

# Reconstruct the data 

X_train_final = stack_samples(train_sentences, vectorizer).T
X_test_final = stack_samples(test_sentences, vectorizer).T
y_train_final = np.expand_dims(y_train, axis = 1).T
y_test_final = np.expand_dims(y_test, axis = 1).T

# Get the dimension for the training part

m, nx, ny = get_dataset_dimensions(X_train_final, y_train_final)
print(f"Number of training samples: {m}\n")
print(f"Number of input features: {nx}\n")

multi_class_classifier = MCC(X_train_final, y_train_final, 10, 0.01, [500, 1000, 1000, 16])
multi_class_classifier.fit()

yhat_test = multi_class_classifier.predict(X_test_final)
yhat_test = np.expand_dims(yhat_test, axis = 1)

print(accuracy_score(y_test_final.T, yhat_test))