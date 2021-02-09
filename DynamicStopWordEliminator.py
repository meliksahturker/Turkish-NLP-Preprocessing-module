#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

class DynamicStopWordEliminator:
    def __init__(self):
        self.stop_words = []
        
    def detect_stop_words(self, input_list, drop_rare_words = False): # takes the output of Tokenizer as input
        unq, cnts = np.unique(input_list, return_counts = True)
        
        if len(unq) < 3:
            raise ValueError('Number of tokens must be at least 3 for Dynamic Stop Word Detection')
            
        df_words = pd.DataFrame({'word': unq, 'counts': cnts}).sort_values(by = 'counts', ascending = False).reset_index(drop = True)
        
        # Adds most frequent words to stop_words list
        argmax_second_der = df_words['counts'].pct_change().abs().pct_change().abs().dropna().idxmax()
        stop_words_extracted = df_words.loc[:argmax_second_der, 'word'].values.tolist()
        self.stop_words += [x for x in stop_words_extracted if x not in self.stop_words]
        
        # Adds frequency 1 words to stop_words list
        if drop_rare_words:
            self.stop_words += df_words.loc[df_words['counts'] == 1, 'word'].values.tolist()
        
        print('Detected stop words for the given corpus are:', stop_words_extracted)
        
    def drop_stop_words(self, input_list):
        return [x for x in input_list if x not in self.stop_words]



