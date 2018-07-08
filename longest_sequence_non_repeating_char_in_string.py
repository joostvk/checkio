# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 13:17:11 2018

@author: JOOST
"""

def longest_unique_sequence(string):
    """
        the longest substring without repeating chars
    """
    max_word = ''
    seen = {}
    maximum_length = 0
    start = 0
    for end in range(len(string)):
        if string[end] in seen:
            start = max(start,seen[string[end]]+1)
        seen[string[end]] = end
        if end - start +1 > maximum_length:
            max_word = string[start:end+1]
        maximum_length = max(maximum_length, end - start +1)
    return max_word    

longest_unique_sequence('12345a123456789')