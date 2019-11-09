# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:28:50 2019

@author: JOOST
"""

num_list = [1,4,3,5,5]
len_list = len(num_list) + 1

max_num = 0
for i in range(len_list):
    for j in range(len_list):
        if j > i:
            print(len(num_list[i:j]), min(num_list[i:j]))
            temp_num = len(num_list[i:j]) * min(num_list[i:j])
            if temp_num > max_num:
                max_num = temp_num
print(max_num)
            
            

def largest_histogram(num_list):
    len_list = len(num_list) + 1
    max_num = 0
    for i in range(len_list):
        for j in range(len_list):
            if j > i:
                print(len(num_list[i:j]), min(num_list[i:j]))
                temp_num = len(num_list[i:j]) * min(num_list[i:j])
                if temp_num > max_num:
                    max_num = temp_num
    return max_num

def largest_histogram(histogram):
    return max(height * max(len(strip) for strip in ''.join('x' if x >= height else ' ' for x in histogram).split()) for height in set(histogram))



Numeral	Value
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)