#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from NaiveBayesClassifier import NaiveBayesClassifier
from sklearn.linear_model import LogisticRegression
PATH = "DATA"
class MLBasedSentenceSplitter:
    def __init__(self):
        self.NBC = NaiveBayesClassifier()
        self.LRC = LogisticRegression()
        nbp = open(PATH + "/" + 'non_breaking_prefixes_tr.txt', mode='r', encoding='utf-8').readlines()
        abbreviations = []
        for line in nbp:
            if line.strip() != '' and line.strip()[0] != "#":
                abbreviations.append(line.strip())
                
        self.abbreviations = abbreviations[1:]
        self.sentence_ending_punctuations = ['.', '!', '?']
        self.quotation_space_starters = ['"', "("]
        self.quotation_space_enders = ['"', ")"]
        
    def create_features(self, string_of_sentences):
        combined_sentences = string_of_sentences
        total_number_of_spaces =  len(combined_sentences.split()) - 1
        location_of_spaces = (pd.Series(combined_sentences.split()).str.len().cumsum().values + np.arange(0, len(combined_sentences.split())))[:-1]

        features = []
        for loc in location_of_spaces:
            # Features
            # - Is previous character sentence ender punctuation?
            # - Is next character capital letter?
            # - Is next character numeric?
            # - Is previous character numeric?
            # - Is previous character quotation mark or closing paranthesis?
            # - Is next character quotation mark or opening paranthesis?
            # - Is previous token am abbreviation from non_breaking_prefixes?

            is_prev_char_sent_ender_punc = combined_sentences[loc - 1] in self.sentence_ending_punctuations
            is_next_char_capital_letter = combined_sentences[loc + 1].isupper()
            is_next_char_numeric = combined_sentences[loc + 1].isnumeric()
            is_prev_char_numeric = combined_sentences[loc - 1].isnumeric()
            is_next_char_quotspace_starter = combined_sentences[loc + 1] in self.quotation_space_starters
            is_prev_char_quotspace_ender = combined_sentences[loc - 1] in self.quotation_space_enders
            is_prev_token_abbreviation = combined_sentences[:loc].split()[-1] in self.abbreviations

            features.append([is_prev_char_sent_ender_punc, is_next_char_capital_letter, is_next_char_numeric, 
                            is_prev_char_numeric, is_next_char_quotspace_starter, is_prev_char_quotspace_ender, 
                            is_prev_token_abbreviation])
        return np.array(features) * 1, location_of_spaces
    
    def create_labels(self, list_of_sentences): # list of sentences
        sentences = list_of_sentences
        total_number_of_spaces = len(" ".join(sentences).split()) - 1
        y = np.zeros(total_number_of_spaces)
        split_positions = (pd.Series(sentences).str.split().str.len().cumsum() - 1).values[:-1]
        y[split_positions] = 1
        return y
    
    def fit(self, list_of_sentences, model = 'NBC'):
        string_of_sentences = " ".join(list_of_sentences)
        X, _ = self.create_features(string_of_sentences)
        y = self.create_labels(list_of_sentences)
        
        if model == 'LogisticRegression':
            self.LRC.fit(X, y)
        else:
            self.NBC.fit(X, y)
        
    def predict(self, string_of_sentences, model = 'NBC'):
        X, location_of_spaces = self.create_features(string_of_sentences)
        if model == 'LogisticRegression':
            preds = self.LRC.predict(X)
        else:
            preds = self.NBC.predict(X)
        return [int(i) for i in preds] 
        
    def split_text_into_sentences(self, string_of_sentences, model = 'NBC'):
        X, location_of_spaces = self.create_features(string_of_sentences)
        
        if model == 'LogisticRegression':
            preds = self.LRC.predict(X)
        else:
            preds = self.NBC.predict(X)
        
        # converting boolean predictions into actual splitted sentences
        boolean_preds = [x == 1 for x in preds]
        indices = [0] + location_of_spaces[boolean_preds].tolist()
        splitted_sentences = [string_of_sentences[i:j] for i,j in zip(indices, indices[1:]+[None])]
        # taking care of whitespace
        splitted_sentences = [sentence if sentence[0] != ' ' else sentence[1:] for sentence in splitted_sentences]
        return splitted_sentences







