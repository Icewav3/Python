# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 08:21:08 2023

@author: coled
"""

members_tuple = (10,20,30,40)
mixed_data_tuple = (2.718,"Green", True, 42)
single_item_tuple = (22,) # comma = tuple
empty_tuple = ()

print("number tuple", members_tuple)
print("mixed data", mixed_data_tuple)

print("\n")

numbers_set = {15,20,25}
print("numbers_set:", numbers_set)

print("\n")

set1 = {1,2,3,4,5,6}
set2 = {10,9,8,7,6,5}
print(set1.intersection(set2))

print("\n")

#This line creates a dictionary of vehicles, as follows:
# my_custom_dictionary = {'subaru': ('green'), 'honda': ('red'), 'ford': ('white')}
my_custom_dictionary = {'vehicles' : ['subaru', 'honda', 'ford'] , 'colors' : ('green', 'red', 'white')}
#This line prints all content in dictionary:
print("my_custom_dictionary:", my_custom_dictionary)

print("\n")
#This line prints only the number of bikes in the dictionary:
print("The valid colors in my dictionary are:", my_custom_dictionary['colors'])