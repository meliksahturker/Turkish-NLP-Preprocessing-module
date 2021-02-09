#!/usr/bin/env python
# coding: utf-8

import numpy as np

class NaiveBayesClassifier:
    def __init__(self):
        
        self.stats = {} # Mean and Standard deviation of each class
        self.lens = {} # Number of data points of each class
        self.total_len = 0 # Total number of data points in train data
        self.number_of_features = None 
        self.classes = None
        self.epsilon = 1e-10 # not to have 0 division error. chosen according to scikit-learn implementation
        self.probs = None
        
    # training
    def fit(self, X, y):
        self.number_of_features = X.shape[1]
        self.classes = np.unique(y)
        
        # for all classes, and all features, calculate and save the mean and standard deviation of each feature
        for cls in self.classes:
            data = X[y == cls]
            means = np.mean(data, axis = 0)
            stds = np.std(data, axis = 0)
            self.lens[cls] = data.shape[0]
            self.total_len += data.shape[0]

            summary = np.concatenate((means, stds)).reshape(2, -1).T
            self.stats[cls] = summary
    
    # predicting
    def predict(self, X):
        y_hat = []
        number_of_rows = X.shape[0]
        
        # for each row(allows batch prediction)
        for row_idx in range(number_of_rows):
            probs = []
            row = X[row_idx, :]
            # for each class
            for cls in self.classes:
                p_cls = self.lens[cls] / self.total_len

                # for each feature
                for i in range(self.number_of_features):
                    mean_of_feature = self.stats[cls][i, 0]
                    std_of_feature = self.stats[cls][i, 1]
                    # if std of a feature is 0, then dont calculate probability for that feature and continue
                    if std_of_feature == 0:
                        continue
                    value_of_feature = row[i]
                    pdf_prob = self.pdf(value_of_feature, mean_of_feature, std_of_feature)
                    # if pdf returns 0 probability, then use epsilon value in log probability.
                    if pdf_prob == 0:
                        pdf_prob = self.epsilon
                    # add the log probability of feature to the sum
                    p_cls += np.log(pdf_prob)
                probs.append([cls, p_cls])
            probs = np.array(probs)
            # get the prediction, taking the argmax or probs
            idx_of_pred = np.argmax(probs[:, 1].astype(float))
            pred = probs[idx_of_pred, 0]
            y_hat.append(pred)
            self.probs = probs
        return y_hat
    
    # probability density function
    def pdf(self, x, mean, stdev):
        expo = np.exp(-((x-mean)**2 / ((2 * stdev**2 ))))
        return (1 / ((np.sqrt(2 * np.pi) * stdev))) * expo
