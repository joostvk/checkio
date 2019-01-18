# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:16:43 2019

@author: JOOST
"""

def from_camel_case(st):
    pass

from_camel_case("MyFunctionName") == "my_function_name"
from_camel_case("IPhone") == "i_phone"
from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
from_camel_case("Name") == "name"

def from_camel_case(string1):
    split_loc = []
    for i,l in enumerate(string1):
        if l.isupper():
            split_loc.append(i)
    split_loc.append(len(string1))        
    
    names_list = []    
    for i in range(len(split_loc)-1):
        names_list.append(string1[split_loc[i]:split_loc[i+1]].lower())
    return ('_'.join(names_list))
            

x = ['GetRidOfThese', 'StupidVarNames']

y = [from_camel_case(i) for i in x]
y