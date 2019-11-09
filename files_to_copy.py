# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:47:12 2019

@author: JOOST
"""

import os
from shutil import copyfile


input_dir =  'C:\\temp'
output_dir = 'C:\\temp2'
file_extension = '.jpg'

files_to_copy = ['20180814_135554', '20180824_204845']
files_to_copy2 = [filename + file_extension for filename in files_to_copy]

for filename in os.listdir(input_dir):
    if filename.endswith(file_extension): 
        if filename in files_to_copy2:
            src = os.path.join(input_dir, filename)
            dst = os.path.join(output_dir, filename)
            copyfile(src, dst)
        # print(os.path.join(directory, filename))
    else:
        continue


files_to_copy = input("Welke bestanden wil je kopieren:")
files_to_copy = files_to_copy.split(',')
