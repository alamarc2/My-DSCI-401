# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import pandas as pd
import numpy as np
from operator import itemgetter
from statistics import mode


class KNN:
    def __init__ (self, K, function):
        self. K = K
        self.function = function
    
    def fit(self, x_train, y_train):
        if isinstance(x_train, pd.DataFrame):
            x_train = x_train.values
        
        xs = []
        ys = []
        counts = 0
        countss = 0
        
        for i in x_train:
            xs.append((i, counts))
            counts = (counts + 1)
            
        for i in y_train:
            ys.append((i,countss))
            countss = (countss + 1)
            
        self.x_train = xs
        self.y_train = ys
        
    def pred(self, x_test):
        if isinstance(x_test, pd.DataFrame):
            x_test = x_test.values
            
        results = []
        
        
        for i in x_test:
            temp = []
            
            for y in self.x_train:
                
            
                lol = ((self.function(i, y[0]), y[1]))
                
                temp.append(lol)
                
                
            temp.sort(key=itemgetter(0))
            temp = temp[:self.K]
            results.append(temp)
        
        
              
        neighbors = []
        for i in results:
            store = []
            store2 = []
            for x in i:
                
                store.append(self.y_train[x[1]])
            
            for i in store:
                store2.append(i[1])
            print(store2)
            neighbors.append(store2)  
            
           
        for i in neighbors:
            for x in i:
                i = self.y_train[x]
                
        preds = [] 
        for i in neighbors:
            
            preds.append(mode(i))
               
        return(preds)    
            
            
#        
            
        
    
    
        

    
  
        