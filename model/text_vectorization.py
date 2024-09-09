from tensorflow.keras.layers import TextVectorization
import random
import pandas as pd 
import numpy as np


def train_tokenizer(train_data, max_tokens, output_sequence_length):

    """
    Adapt a TextVectorization layer on the provided training data.

    Parameters:
    - train_data: An iterable of text strings used for training the tokenizer.
    - max_tokens: The maximum number of tokens to consider.
    - output_sequence_length: The length of the output sequences.

    Returns:
    - A trained TextVectorization layer.
    """
        
    text_vectorizer = TextVectorization(max_tokens=max_tokens, output_sequence_length=output_sequence_length)
    text_vectorizer.adapt(train_data)
    return text_vectorizer 

def random_vectorized_sample(data, text_vectorizer):

    """
    Print a random sample from the data and its vectorized representation.

    Parameters:
    - data: An iterable of text strings used for sampling.
    - text_vectorizer: A trained TextVectorization layer.

    Returns:
    - None
    """

    target_sentence = random.choice(data)
    print(f"Text:\n{target_sentence}")
    print(f"\nLength of text: {len(target_sentence.split())}")
    print(f"\nVectorized text:\n{text_vectorizer([target_sentence])}")
    print(f"\nVectorized text shape: \n {text_vectorizer([target_sentence]).shape}")


def stack_samples(text_data, text_vectorizer):

    """
    Process and vectorize text data using the provided TextVectorization layer.

    Parameters:
    - text_data: A 1D NumPy array or list of text strings, where each element is a text string to be vectorized.
    - text_vectorizer: A trained TextVectorization layer used to convert text into numerical vectors.

    Returns:
    - A NumPy array of shape (output_seq_len, len(text_data)), where output_seq_len is the length of the vectorized output sequence.
    """

    text_data_array = np.array(text_data)
    text_data_expanded = np.expand_dims(text_data_array, axis=1)
    vectorized_data = text_vectorizer(text_data_expanded)
    vectorized_data_array = np.array(vectorized_data)
    return vectorized_data_array
    
    

    