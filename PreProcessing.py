#!/usr/bin/env python
# coding: utf-8

from RuleBasedSentenceSplitter import RuleBasedSentenceSplitter
from NaiveBayesClassifier import NaiveBayesClassifier
from DynamicStopWordEliminator import DynamicStopWordEliminator
from MLBasedSentenceSplitter import MLBasedSentenceSplitter
from Normalizer import Normalizer
from Stemmer import Stemmer
from RuleBasedTokenizer import RuleBasedTokenizer
from StaticStopwordRemover import StaticStopwordRemover
from MLBasedTokenizer import MLBasedTokenizer

import pandas as pd
from sklearn import metrics
PATH = "DATA"

class PreProcessing:
    def __init__(self):
        
        self.NaiveBayesClassifier = NaiveBayesClassifier()
        
        # Sentence Splitters
        self.RuleBasedSentenceSplitter = RuleBasedSentenceSplitter()
        self.MLBasedSentenceSplitter = MLBasedSentenceSplitter()
        
        # Tokenizers
        self.RuleBasedTokenizer = RuleBasedTokenizer()
        self.MLBasedTokenizer = MLBasedTokenizer()
        
        # Normalizer
        self.Normalizer = Normalizer()
        
        # Stemmer
        self.Stemmer = Stemmer()
        
        # Stopword Eliminators
        self.StaticStopWordEliminator = StaticStopwordRemover()
        self.DynamicStopWordEliminator = DynamicStopWordEliminator()


    def all_metrics_together(self, y, y_hat):
        accuracy = metrics.accuracy_score(y, y_hat)
        recall = metrics.recall_score(y, y_hat)
        precision = metrics.precision_score(y, y_hat)
        f1 = metrics.f1_score(y, y_hat)

        df = pd.DataFrame({'Accuracy': accuracy, 'Recall': recall, 'Precision': precision, 'F1': f1}, index = ['Score'])
        return df
