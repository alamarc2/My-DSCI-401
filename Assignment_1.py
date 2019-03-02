# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



#Andrew LaMarca Assignment 1

a = [1,2,3]        
b = ['a','b']
c = [5,6,7]

def flatten(*old_list):
    if old_list == []:
        return([])                     #bayes case
    new_list = []                      #empty list
    for i in old_list:                 #loop through arguments
        if type(i) ==  'list':         #if you have a nested list this will go into it
            new_list.extend(flatten(i))#and this will recursively go through each nested list until it is not a list
        else:
            new_list.extend(i)
            
    return new_list
            
def all_perms(lst):
    if len(lst) == 0:                #bayes case
        return([[]])
    if len(lst) == 1:                #bayes case
        return([lst])
    else:
        store = []                   #list that will store our permutations
        for i in range(len(lst)):
            x = lst[i]               #our index position 
            y = lst[:i] + lst[i+1:]  #up to but not including our index and [i+1] so that position will change 
            for j in all_perms(y):   #recursively looping through each set of combinations other than our i position
                store.append([x]+j)  #and adding it to each of our original indexs lst[i] i.e. for (1,2,3) it extends every combination of all indexes to 1, 2, and 3
        return(store)
        
def powerset(lst):
    l = [[]]                         #empty nested list
    for i in lst:
        base = [j + [i] for j in l]  #using a list comprehension to build up powerset for each index in original list, after first iteration nested list goes away, after second j changes to index i and this happens for the length of the list
        l.extend(base)
    return(l)    
        
                

      

