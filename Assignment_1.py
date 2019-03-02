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
        
def spiral(n, corner):
    #For my spiral I worked closely with Colin Grosh. We came close but were unable to perfectly produce the desired output.
    # Define the directions depending on each corner, number = corner we want the spiral to end in
    one_dir = [(0,-1), (1,0), (0,1), (-1,0), ()]
    two_dir = [(-1,0), (0,-1), (1,0), (0,1), ()]
    three_dir = [(1,0), (0,1), (-1,0), (0,-1), ()]
    four_dir = [(0,1), (0,-1), (0,-1), (1,0), ()]

    # Choose which direction set to use depending on what corner is entered
    if corner == 1:
        dir = one_dir.copy()
    elif corner == 2:
        dir = two_dir.copy()
    elif corner == 3:
        dir = three_dir.copy()
    elif corner == 4:
        dir = four_dir.copy()
    else:
        return "Corner must be within 1 and 4"

    use = n
    q = n**2
    changes = []
    count = n
    start = q-n
    other = (n**2)-1
    changes.append(start)

    # Get all the values in the matrix where the direction will change
    while count != 1:
        x = start - (n-1)
        y = x - (n-1)
        changes.append(x)
        changes.append(y)
        count -= 1
        n -= 1
        start = y

    value = []
    directions = []
    dir_index = 0

    # Get the values and the direction of each value depending on where is located
    while other > 0:
        if other in changes:
            value.append(other)
            directions.append(dir[dir_index])
            dir_index +=1
            if dir_index > 3:
                dir_index = 0
            other -= 1
        else:
            value.append(other)
            directions.append(dir[dir_index])
            other -= 1

    # Build an empty matrix
    matrix = [[0] * use for i in range(use)]

    # Determine where the first value will start based on the specified corner
    n = use
    if corner == 1:
        n_x = 0
        n_y = 0
    elif corner == 2:
        n_x = 0
        n_y = n-1
    elif corner == 3:
        n_x = n-1
        n_y = 0
    elif corner == 4:
        n_x = n-1
        n_y = n-1

    # Loop through and append the values to the matrix
    # Add on to the index
    for i in range(0, (n**2)-2):
        print('it ran ', value[i])
        matrix[n_x][n_y] = value[i]
        if value[i] == 0:
            break
        else:
            n_x += directions[i+1][0]
            n_y += directions[i+1][1]
    for i in matrix:
        print(i)

     #The output does not perfectly match the spiral but the center is zero and the end position in the corner is correct.          
     #Something is wrong with the way the direction changes move the values. Possibly due to misunderstanding of 
     #matrix positioning
 

