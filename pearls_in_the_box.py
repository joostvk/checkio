# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 15:50:44 2018

@author: JOOST
"""
#def checkio(marbles, num):
#    pass
#
#checkio('bbw', 3) == 0.48
#checkio('wwb', 3) == 0.52
#checkio('www', 3) == 0.56
#checkio('bbbb', 1) == 0
#checkio('wwbb', 4) == 0.5
#checkio('bwbwbwb', 5) == 0.48
#
#
#


marbles = 'bbw' 
len(marbles)

comp = [{'d':0, 'w':0, 'b':3, 'c' :1}]
comp2 = []
comp3 = []
t = comp2 + comp3



def return_marbles(mb_stat):
    mb_stat_ret_tmp0, mb_stat_ret_tmp1, mb_stat_ret_tmp2 = [], [], []
    nr_white = mb_stat['w'] 
    nr_black = mb_stat['b']
    mb_stat_ret = mb_stat['ds'] + 1
    if mb_stat['w'] == 0:
        mb_stat_ret_tmp0 = {'ds': mb_stat_ret, 'w' : 1, 'b' : nr_black -1, 'c' : mb_stat['c'] * (nr_black -1 / nr_black)}
    if mb_stat['b'] == 0:
        mb_stat_ret_tmp0 = {'ds': mb_stat_ret, 'w' : nr_white -1, 'b' : 1, 'c' : nr_white -1 / nr_white}
    if mb_stat['w'] > 0 and mb_stat['b'] > 0:
         mb_stat_ret_tmp1 = {'ds': mb_stat_ret, 'w' : nr_white +1, 'b' : nr_black -1, 'c' : mb_stat['c'] * nr_black / (nr_black + nr_white)}
         mb_stat_ret_tmp2 = {'ds': mb_stat_ret, 'w' : nr_white -1, 'b' : nr_black +1, 'c' : mb_stat['c'] * nr_white / (nr_black + nr_white)}
    return([mb_stat_ret_tmp0 + mb_stat_ret_tmp1 + mb_stat_ret_tmp2])


comp = [{'ds':0, 'w':0, 'b':3, 'c' : 1}]
return_marbles(comp[0])



for n, status in enumerate(comp):
    print(n,status)
    if status['w'] == 0:
        comp.append({'ds': n, 'w':1, 'b':2, 'c' : 2/3})   
    if status['b'] == 0:
        comp.append({'ds': n, 'w':2, 'b':1, 'c' : 2/3})   
    else:
        whites  = comp[0]['b']
        comp.append({'ds': n, 'w': whites, ' b' : blacks, 'c': whites/blacks})


comp['w']






draws = dict{'d0' : }
#for i in range(1,4,1):
#    print(i)
#    
#x.count('w') / 3
#
#
## voorspel de kans op de volgende staat
#
## 1/3 kans op bbb
#    # 3/3 kans op wbb
#    # 0 kan op bbb
## 2/3 kans op bww
#
## we loopen keer door iedere
## state, chance
#    
#list = [('wwb' , 1)]    
#
#for i in range(1,3,1):
#    print('item' + str(i))
#    
#pos = {'iter1' : ['wbb', .9]}
#
#for x in range(1,3,1):
#    print(pos)

count_word = {}
zin  = 'ik ik ga mee'
for i,j in enumerate(zin.split()):
    if j in count_word:
        count_word[j] += 1
    else:
        count_word[j] = 1
    

