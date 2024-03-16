## Topic 1: Tokenization

## Importing the required libarires for tokenization - 
### Using tensorflow library

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = ["I love Allah (swt)", "Allah is the creator"]

print(sentences)

tokenizer = Tokenizer(num_words = 100)

tokenizer.fit_on_texts(sentences)

words_dictionary = tokenizer.word_index

print(words_dictionary)
