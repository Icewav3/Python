# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 08:40:53 2023

@author: coled
"""

import random

max = 100000

solved = False

ans = random.randint(0,max)
count = 0


while solved == False:
    guess = random.randint(0,max)
    count+=1
    
    if guess==ans:
        print(f"guessed correctly, answer was {ans}")
        print("\n")
        print(f"It took {count} guesses to guess the correct answer")
        solved = True
    else:
        print(f"{guess} was incorrect")
        
        
# def add(var, var2):
#     return var+var2
# print(add(1,8))