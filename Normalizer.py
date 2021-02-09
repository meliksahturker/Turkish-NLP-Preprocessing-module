#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
import numpy as np
import string
from num2words import num2words
PATH = "DATA"
# Multiword Lexicon
mwe = pd.read_csv(PATH + "/"+'MWE_lexicon.txt', sep = "\n", error_bad_lines=False, header = None).values.reshape(-1).tolist()

# General Purpose Typo, Abbreviation, Social Media, etc. Normalization Lexicon
df = pd.read_csv(PATH + "/"+'typo_correction_lexicon.txt', sep = "\n", na_filter = False, header = None, error_bad_lines= False)
df = df[0].str.split("=", expand = True)
df = pd.concat([df[0], df[1].str.split(',', expand = True)], axis = 1).iloc[:, 0:2]
df.columns = ['typo', 'correct']
df = df.iloc[500:,:].reset_index(drop = True)

# Word Lexicon merged from TDK-Zemberek, Zargan, Bilkent Creative Writing, Turkish Broadcast News
words_lexicon = pd.read_csv(PATH + "/"+'merged_words_lexicon.csv', na_filter = False).values.reshape(-1).tolist()


# https://stackoverflow.com/questions/2460177/edit-distance-in-python
def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


class Normalizer():
    def __init__(self):
        self.words_lexicon = words_lexicon
        self.mwe_lexicon = mwe
        self.general_purpose_lexicon = df
        
        self.vowels = set("aeiou")
        self.consonants = set(string.ascii_lowercase) - self.vowels
        self.non_turkish_accent_marks = {'â':'a', 'ô':'o', 'î':'ı', 'ê':'e', 'û':'u'}
    
    def remove_punctuations(self, token):
        return ''.join([t for t in token if t not in string.punctuation])
    
    def convert_to_lower_case(self, token):
        return token.lower()
    
    def convert_number_to_word(self, number):
        return num2words(number, lang = 'tr')
    
    def remove_accent_marks(self, token):
        return ''.join(self.non_turkish_accent_marks.get(char, char) for char in token)
    """
    def multiword_replace(self, token):
        if token in self.mwe_lexicon['corrected_expression'].values:
            return token
        elif token in self.mwe_lexicon['original_expression'].values:
            return self.mwe_lexicon['corrected_expression'][self.mwe_lexicon['original_expression'] == token].values[0].split(' ')
        else:
            return token
    """
    
    def general_purpose_normalize_by_lexicon(self, token):
        if token in self.words_lexicon:
            return token
        elif token is self.general_purpose_lexicon['typo'].values:
            return self.general_purpose_lexicon['correct'][self.general_purpose_lexicon['typo'] == token].values[0]
        else:
            return token
    
    def return_most_similar_word(self, s1):
        s1_consonant = "".join([l for l in s1 if l in self.consonants])
        distance_list = []
        consonant_distance_list = []

        for s2 in self.words_lexicon:
            dist = levenshtein_distance(s1, s2)
            distance_list.append(dist)

            s2_consonant = "".join([l for l in s2 if l in self.consonants])
            consonant_dist = levenshtein_distance(s1_consonant, s2_consonant)
            consonant_distance_list.append(consonant_dist)

        df_sorted = pd.DataFrame({'Distance': distance_list, 'Consonant_Distance': consonant_distance_list}).sort_values(by = ['Consonant_Distance', 'Distance'])
        most_similar_word = self.words_lexicon[df_sorted.index[0]]

        return most_similar_word
        
    # High Level Function
    def normalize(self, list_of_tokens):
        normalized_list_of_tokens = []
        
        for token in list_of_tokens:
            token = self.remove_punctuations(token)
            token = self.convert_to_lower_case(token)
            if token in self.mwe_lexicon:
                return token
            
            if token.isnumeric():
                token = self.convert_number_to_word(float(token))
                normalized_list_of_tokens.append(token)
                continue
  
            token = self.remove_accent_marks(token)
            token = self.general_purpose_normalize_by_lexicon(token)
        
            if token not in self.words_lexicon:
                token = self.return_most_similar_word(token)
            if token != '':
                normalized_list_of_tokens.append(token)
        
        return normalized_list_of_tokens