# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 10:31:04 2019

@author: JOOST
"""

import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #test areas when radius >-
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(1),pi)
        

def test_values(self):
    # check value errors