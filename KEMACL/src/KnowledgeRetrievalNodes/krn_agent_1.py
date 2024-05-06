from absl import app, flags
from absl.flags import FLAGS
import os
import sys
import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import LSTM, Embedding, Dense, Input, Flatten, Dropout, Bidirectional
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

FLAGS = flags.FLAGS
flags.DEFINE_string('data_dir', '', 'Path to data directory')
flags.DEFINE_string('output_dir', '', 'Path to output directory')
flags.DEFINE_integer('max_length', 100, 'Maximum sequence length')
flags.DEFINE_integer('vocabulary_size', 50000, 'Size of vocabulary')
flags.DEFINE_float('dropout_rate', 0.2, 'Dropout rate for LSTM layers')
flags.DEFINE_string('embedding_file', '', 'Path to pre-trained word embeddings file')
flags.DEFINE_integer('num_layers', 1, 'Number of LSTM layers')
flags.DEFINE_boolean('bidirectional', False, 'Use bidirectional LSTMs')
flags.DEFINE_string('model_file', '', 'Path to saved model file')

class KRNAgent:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.max_length = FLAGS.max_length
        self.vocabulary_size = FLAGS.vocabulary_size
        self.dropout_rate = FLAGS.dropout_rate
        self.embedding_file = FLAGS.embedding_file
        self.num_layers = FLAGS.num_layers
        self.bidirectional = FLAGS.bidirectional
        self.output_dir = FLAGS.output_dir

    def load(self):
        print('Loading model...')
        with open(os.path.join(self.output_dir, 'model.pickle'), 'rb') as f:
            self.model = pickle.load(f)
        with open(os.path.join(self.output_dir, 'tokenizer.pickle'), 'rb') as f:
            self.tokenizer = pickle.load(f)

    def save(self):
        print('Saving model...')
        with open(os.path.join(self.output_dir, 'model.pickle'), 'wb') as f:
            pickle.dump(self.model, f)
        with open(os.path.join(self.output_dir, 'tokenizer.pickle'), 'wb') as f:
            pickle.dump(self.tokenizer, f)

    def train(self):
        print('Training model...')
        # Load data
        with open(os.path.join(FLAGS.data_dir, 'train.pkl'), 'rb') as f:
            train = pickle.load(f)
        with open(os.path.join(FLAGS.data_dir, 'test.pkl'), 'rb') as f:
            test = pickle.load(f)
        # Create tokenizer
        self.tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=self.vocabulary_size, oov_token='<UNK>')
        self.tokenizer.fit_on_texts(train['text'])
        train_sequences = self.tokenizer.texts_to_sequences(train['text'])
        test_sequences = self.tokenizer.texts_to_sequences(test['text'])
        # Pad sequences to maximum length
        max_length = max([len(sequence) for sequence in train_sequences]) + 1
        self.max_length = max_length
        train_sequences = pad_sequences(train_sequences, maxlen=max_length)
        test_sequences = pad_sequences(test_sequences, maxlen=max_length)
        # Create model
        input_layer = Input(shape=(self.max_length,))
        embeddings = Embedding(input_dim=self.vocabulary_size + 1, output_dim=64,
        input_length=max_length)(input_layer)
        lstm = LSTM(32, dropout=self.dropout_rate, recurrent_dropout=self.dropout_rate)(embeddings)
        dense = Dense(128, activation='relu')(lstm)
        output = Dense(self.vocabulary_size + 1, activation='softmax')(dense)
        model = Model(inputs=input_layer, outputs=output)
        # Compile model
        optimizer = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0)
        model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        # Train model
        history = model.fit(train_sequences, train['label'], epochs=10, batch_size=64, validation_split=0.2)
        print('Evaluating model...')
        loss, accuracy = model.evaluate(test_sequences, test['label'])
        print(f'Test loss: {loss}, Test accuracy: {accuracy}')
        # Save model and tokenizer
        self.model = model
        self.tokenizer = self.tokenizer
        self.save()