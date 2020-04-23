# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:19:45 2020

@author: VicFabrice
"""

## Hi, welcome to Another day studying random stuff - Technical Interview Edition ##

# Today I'm going to begin with this post https://pynative.com/python-data-structure-exercise-for-beginners/
# about Data structures in Python
# Days after I was wondering if trees were a thing in Python, I mean, I spent a lot of time
#learning trees in college and what now? Did I waste my time? Possibly, but It doesn't matter

#So...The post describes 10 exercises, I'm guessing It covers only build-in types:
#Lists, Tuples and dictionaries. But stop guessing and start coding 

###### 1 ####### 
#Question 1: Given a two list. Create a third list by picking an odd-index 
#element from the first list and even index elements from second.

###############

# Example lists (Given list != Input List)

listOne = [1,2,3,4,5,6,7]
listTwo = [8,9,10,11,12,13,0]

def oddIndex(xs):
    return list(filter(lambda x : (xs.index(x) % 2) > 0, xs))

def evenIndex(xs):
    return list(filter(lambda x : (xs.index(x) % 2) == 0, xs))
    
 
print("Testing odd index ",oddIndex(listOne))
print("Testing even index ",evenIndex(listTwo))

#Nice and explanatory but not-too-short fc name
def oddIndexElementsFromFirstListAndEvenFromSecond(xs,ys): 
    return oddIndex(xs) + evenIndex(ys)

oddInd = oddIndex(listOne)
evenInd = evenIndex(listTwo)
result = oddIndexElementsFromFirstListAndEvenFromSecond(listOne,listTwo)
print("Odd index numbers list: {}\n Even index numbers list: {}\n Resulting list: {}".format(oddInd,evenInd,result))
    
        