# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 20:21:34 2019

@author: JOOST
"""

def abs_sorting(num_list: tuple) -> list:
    """
    The list or tuple (but not a generator) sorted by absolute values in ascending order.
    """
    neg_list = [i for i in num_list if i < 0]
    abs_list = [abs(i) for i in num_list]
    abs_list.sort()
    return [i * -1 if -i in neg_list else i for i in abs_list]



abs_sorting((-20, -5, 10, 15)) == [-5, 10, 15, -20] # or (-5, 10, 15, -20)
abs_sorting((1, 2, 3, 0)) == [0, 1, 2, 3]
abs_sorting((-1, -2, -3, 0)) == [0, -1, -2, -3]
print("joost")



abs_sorting([1,23,-5])

def abs_sorting2(num_list: tuple) -> list:
    return sorted(num_list, key=abs)

abs_sorting2([1,23,-5])