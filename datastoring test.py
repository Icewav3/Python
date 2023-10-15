# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 09:34:59 2023

@author: coled
"""
parent_matrix = []
matrix_x = []
matrix_y = []

# Read the input from the user
input_str = input("Enter a position (in the format '31, 1'): ")
input_str = input("Input: ")
# Split the input string using the comma as the delimiter
try:
    x, y = map(int, input_str.split(','))
    
    print(f'x: {x}, y: {y}')
except ValueError:
    print("Invalid input format. Please use 'x, y' format.")


class MatrixManager:
    
    def ExtendMatrix(list parent_matrix, int value):
        parent_matrix.len()
        matrix.append()
        return matrix
    