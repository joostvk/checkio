# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:43:16 2019

@author: JOOST
"""

# two sum problem python

#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

#class Solution(object):

def twoSum(nums, target):
    index = {}
    j = 1
    for i, x in enumerate(nums):
        check = target - x
        if check in index:
            return [index[check] + 1, i + 1]
        else:
            index[x] = i       
    return (i,j)




index = {}
for i, x in enumerate(nums):
    print('i and x: ',i,x)
    check = target - x
    if check in index:
        print ([index[check] + 1, i + 1])
    else:
        index[x] = i       

def twoSum(nums,target):
    n=len(nums)
    for i in range(n):
        x=target-nums[i]
        if x in nums and nums.index(x)!=i:
            return [i,nums.index(x)]
        
nums = [12, 7, 11, 15, 100, 200] 
target = 300

twoSum(nums,target)