#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from NaiveBayesClassifier import NaiveBayesClassifier
from sklearn.linear_model import LogisticRegression
import Utility

class MLBasedTokenizer:
    def __init__(self):
        self.NBC = NaiveBayesClassifier()
        self.LRC = LogisticRegression()
        abbreviations = []

        self.abbreviations = abbreviations[1:]
        self.punctuations1 = ['!', '?', ',','"','(',')'] #Always token
        self.punctuations2 = ['.', ':']      #Ambiguous
        self.split_characters = [' ']

    def create_features(self, string_of_sentences):

        # String of sentences = all tokens made into a string.

        combined_sentences = string_of_sentences

        features = []
        length = len(combined_sentences)

        # For all inputs check for features
        # For all inputs create a feature list
        # features = (input number, feature #)
        # Think of every character as input
        # Check every character (except first and last one)

        for index in range(0, length - 1):
            # Features
            # - Is next character a splitter?
            # - Is next character a punctuation?
            # - Is character a punctuation?

            # - Is previous character quotation mark or closing paranthesis?
            # - Is next character quotation mark or opening paranthesis?

            is_next_char_splitter = combined_sentences[index + 1] in self.split_characters

            is_prev_char_punc = combined_sentences[index - 1] in self.punctuations1
            is_next_char_punc = combined_sentences[index + 1] in self.punctuations1

            is_prev_char_punc2 = combined_sentences[index - 1] in self.punctuations2
            is_next_char_punc2 = combined_sentences[index + 1] in self.punctuations2
            is_char_punc2 = combined_sentences[index] in self.punctuations2

            is_prev_char_numeric = combined_sentences[index-1].isnumeric()
            is_char_numeric = combined_sentences[index].isnumeric()
            is_next_char_numeric = combined_sentences[index+1].isnumeric()

            if index + 2 <= index:
                is_next_next_char_numeric = combined_sentences[index + 2].isnumeric()
            else:
                is_next_next_char_numeric = is_char_numeric

            features.append([is_next_char_splitter,
                             is_next_char_punc,
                             is_prev_char_punc,
                             is_next_char_punc2,
                             is_prev_char_punc2,
                             is_char_punc2,
                             is_prev_char_numeric,
                             is_next_char_numeric])


        #print(np.array(features) * 1)
        return np.array(features) * 1

    def create_labels(self, string_of_sentences):  # list of sentences

        # Create labels for all inputs (characters)
        # Except first and last character.

        length = len(string_of_sentences)
        input_length = length - 1
        y = np.zeros(input_length)

        # Create labels based on whether the character is a split or not.

        split_positions = []
        for index in range(0, length - 1):
            if string_of_sentences[index] == ' ':
                split_positions.append(index-1)
            if string_of_sentences[index] == ',':
                split_positions.append(index-1)

            if string_of_sentences[index] == ')':
                split_positions.append(index-1)
            if string_of_sentences[index] == '(':
                split_positions.append(index+1)

            if string_of_sentences[index] == '.':
                if not string_of_sentences[index-1].isnumeric():
                    if not string_of_sentences[index+1].isnumeric():
                        split_positions.append(index - 1)

        # Insert labels to y:
        for position in split_positions:
            if position < input_length:
                y[position] = 1

        # Labeller okey, şuan merhaba. ayır diyor,
        # 22.12 ayırma diyor.

        return y

    def fit(self, string_of_sentences, model='NBC'):

        X = self.create_features(string_of_sentences)
        y = self.create_labels(string_of_sentences)

        if model == 'LogisticRegression':
            self.LRC.fit(X, y)
        else:
            self.NBC.fit(X, y)
        return X, y

    def predict(self, string_of_sentences, model='NBC'):
        X = self.create_features(string_of_sentences)
        if model == 'LogisticRegression':
            preds = self.LRC.predict(X)
        else:
            preds = self.NBC.predict(X)
        return [int(i) for i in preds]


    def split_to_tokens(self, string_of_sentences, model='NBC'):

        X = self.create_features(string_of_sentences)
        splitted_sentences = string_of_sentences

        if model == 'LogisticRegression':
            preds = self.LRC.predict(X)
        else:
            preds = self.NBC.predict(X)

        # converting boolean predictions into actual splitted tokens

        length = len(preds) # Equals to input length
        split_locations = [0]
        tokens = []

        for index in range(length):
            if preds[index] == 1:
                split_locations.append(index+1)
                splitted_sentences = splitted_sentences[:index+1] + '*' + splitted_sentences[index+2:]

            if index == length-1 and preds[index] == 0:
                split_locations.append(index+2)

        length = len(split_locations)

        for index in range(length-1):
            token = string_of_sentences[split_locations[index]:split_locations[index+1]]
            if token == ' ':
                token = string_of_sentences[split_locations[index]+1:split_locations[index+1]+1]
                split_locations[index+1] = split_locations[index+1]+1
            tokens.append(token)

        # Check for the last character
        if preds[len(preds)-1] == 1:
            tokens.append(string_of_sentences[-1])


        return tokens



def main():

    #test_sentence1 = "merhaba. nasılsınız? Ben 22.12.1996 (gününde) !Eskişehir'den 20:02 treniyle geldim."
    test_sentence2 = "merhaba. merhaba.merhaba. merhaba. merhaba. .merhaba. merhaba. merhaba. merhaba. merhaba."

    #tokenization_corpus = Utility.load_file('handmade_turkish_blog_corpus.txt')

    #tokenizer = MLBasedTokenizer()

    #tokenizer.fit(tokenization_corpus, model='NBC')
    #tokenizer.fit(tokenization_corpus, model='LogisticRegression')

    #print('Original sentence is:', test_sentence1)
    #print('Naive Bayes result:', tokenizer.split_to_tokens(test_sentence1, model='NBC'))
    #print('LogisticRegression result:', tokenizer.split_to_tokens(test_sentence1, model='LogisticRegression'))


if __name__ == '__main__':
    main()

