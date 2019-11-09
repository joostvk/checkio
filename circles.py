# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 10:22:36 2019

@author: JOOST
"""

#unit test

from math import pi


def circle_area(r):
    return pi*(r**2)

# test function
radii = [2,0,-3,2+5j, True, 'radius']

message = "Area of circles with r = {} is {}"
for radius in radii:
    A = circle_area(radius)
    print(message.format(radius,A))