# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:30:50 2022

@author: Vincent Medrano
"""

# write function "make_Fibonnaci" that returns first n Fibonnaci numbers.
# put function in module called fibonacci.

def make_Fibonnaci(n):
   if n <= 1:
       return n
   else:
       return(make_Fibonnaci(n-1) + make_Fibonnaci(n-2))


# Test block for first 20 Fibonnaci Numbers
n = 20
for i in range(n):
    print(make_Fibonnaci(i))
    
