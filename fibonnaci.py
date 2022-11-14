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
   
# Johannes Kepler (yes, that Johannes Kepler) claimed that the ratio of
# consecutive Fibonacci numbers converges to the golden ratio.
# Golden Ratio: F[N+1]/F[N] -> (read, 'gets close to  as N increases' )(1+sqrt(5))/2
# Extend your module by defining a function 'converging_ratios'
# that takes an array or list F that contains Fibonacci numbers as input
# and tests to see if Kepler's claim seems correct.
# Put a call to the function in the test block and run the function.
# 'Rate of convergence' is a mathematical concept that shows up in math
# and engineering.
# if e[N] is the difference between the ratio you compute and the golden ratio
# F[N+1]/F[N} - golden ratio =  e[N} = C*e[N}**q, C is some constant,
# then q is the rate of convergence   The computation for q is
# q = np.log(e[N+1]/e{N]) / np.log(e[N]/e[N-1])
# Extend your module by including a function 'computre_rates'
# that  takes a sequence F, and computes the corresponding values
# for q and prints the last 5 values. You do not need any value for C,
# The convergence rates should get close to 1 and N gets large.
def converging_ratios(n):
    a=1
    b=1    
    
    for i in range(n):
        a, b = b, a + b
        print(b * 1.0 / a)
    

# Test block for first 20 Fibonnaci Numbers
n = 20

for i in range(n):
    print(make_Fibonnaci(i))
    
print("\n ---------------BREAKPOINT----------------\n")
    
print(converging_ratios(n))
    
