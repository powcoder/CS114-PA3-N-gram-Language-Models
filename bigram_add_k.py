https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# CS114 Spring 2020 Programming Assignment 3
# N-gram Language Models

from collections import defaultdict
from languageModel import LanguageModel
import numpy as np
from scipy.sparse import lil_matrix

class BigramAddK(LanguageModel):

    def __init__(self):
        self.word_dict = {}
        self.total = None
        self.prob_counter = None
        self.k = 1
    
    '''
    Trains a bigram-add-k language model on a training set.
    '''
    def train(self, trainingSentences):
        # your code here
        pass
    
    '''
    Returns the probability of the word at index, according to the model, within
    the specified sentence.
    '''
    def getWordProbability(self, sentence, index):
        return 0

    '''
    Returns, for a given context, a random word, according to the probabilities
    in the model.
    '''
    def generateWord(self, context):
        return 'kitty'