# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 11:44:26 2018

@author: JOOST
"""

import random
    
def random_walk(n):
    x, y = 0,0
    for i in range(n):
        (dx, dy)= random.choice([(0,1), (0,-1), (1,0),(-1,0)])
        x += dx
        y += dy
#    return (x,y)
    return abs(x) + abs(y)


number_of_walks = 1000

for walk_length in range(1,31):
    no_transport = 0
    
for walk_size in range(10,26):
    transport_home = 0    
    wrong_guess = 20000
    for i in range(wrong_guess):
        if random_walk(walk_size) > 4:
            transport_home += 1
    print ("walk_size: ", walk_size, " gives ",  transport_home / wrong_guess)        

x = [100, 200]
y = [300, 400]

squares2 = [i**2 >10000 for i in x]




import csv

random_words = []
with open('c:\\tmp\\random_text.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        random_words.append(row)
random_words = [item for sublist in l for item in sublist]


import string
alfabet = dict.fromkeys(string.ascii_lowercase, 0)

word = 'jannekerules'
guess_list = []
for i in word:
    guess_list.append('_')
wrong_guess = 0
counter = 0
letters_right = 0



def input_letter():
    letter = ''
    while len(letter) != 1:
        letter = input('what letter do you guess?\n').lower()
    return letter


letter = input_letter()

while wrong_guess < 5:
    letter = input_letter()
    counter += 1
    if letter not in word:
        wrong_guess += 1
    else:
        letters_right += 1
    if alfabet[letter] >= 1:
        print('you guessed that letter already moron')
    else:
        alfabet[letter] +=1
    for teller, letter in enumerate(word):
        if alfabet[letter] > 0:
            guess_list[teller] = letter
        else:
            guess_list[teller] = '_' 
    if '_' not in guess_list:
        print('jaa, goed geraden')
        break
    
    print (guess_list)        
    print ('you guessed ', letters_right, 'times right from ', counter)
    if wrong_guess > 7:
        print('you lost')
        break
    
guess = []

for i in guess_list:
    print(i, end=" ")


between_markers('What is >apple<', '>', '<') == 'apple'
between_markers('No[/b] hi', '[b]', '[/b]') == 'No'


You are given a string and two markers (the initial and final). 
You have to find a substring enclosed between these two markers. But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker then the beginning should be considered as the beginning of a string.
If there is no final marker then the ending should be considered as the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker is standing in front of the initial one then return an empty string.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

Precondition: can't be more than one final marker and can't be more than one initial

sen = 'What is >apple<'
first = '>'
last =  '<'

sen.find(last)
first[9:14]
first[sen.find(first):sen.find(last)]

def between_markers(sen, first, last):
    if first == last:
        return ""
    if first in sen and last in sen:
        return sen[sen.find(first)+len(first):sen.find(last)]
    elif first in sen:
         return sen[sen.find(first)+len(first):]
    elif last in sen:
        return sen[:sen.find(last)]
    else:
        return(sen)


print(between_markers('What is >apple<', '>', '<'))
print(between_markers('What is >apple<', '>', '<>'))
print(between_markers('What is >apple<', '<', '>'))
print(between_markers('What is >apple<', '^', '&'))
    
    

best_stock = {
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }


best_stock_value = max(best_stock.values())
for stock in best_stock:
    if best_stock[stock] == best_stock_value:
        print(stock)






def best_stock(best_stock):
    best_stock_value = max(best_stock.values())
    for stock in best_stock:
        if best_stock[stock] == best_stock_value:
            return(stock)



if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
    


popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
    'i': 4,
    'was': 3,
    'three': 0,
    'near': 0
}

pop_word = {
    'i': 4,
    'was': 3,
    'three': 0,
    'near': 0
}

if 'sdf'in pop_word:
    print('ja hoor')
else:
    print('niet aanwezig')


tekst = '''
When I was One
I had just begun
When I was Two
I was nearly new
'''
tekst = tekst.lower().split()
tekst[0].lower()

words =  ['one','i','nearly']
word_dict = {}
word_dict['i'] = 1


for i in tekst:
    if i in words:
#        print(i)
        word_dict[i] += 1

def popular_words(text, words):
    word_dict = {}
    for word in words:
        word_dict[word] = 0
    text = text.lower().split()
    for word in text:
        if word in words:
            word_dict[word] += 1
    return word_dict
            
tekst = '''
When I was One
I had just begun
When I was Two
I was nearly new
'''
words =  ['one','i','nearly', 'when']   

word_dict = popular_words(tekst, words)



########################################
########################################
########################################
########################################
list_dict = [
        {"name": "oil", "price": 2},
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}]



#for i in list_dict:
#    print(i['name'],i['price'])

def bigger_price(nr, list_dict):
    def sort_key(d):
        return d['price']
    list_dict = sorted(list_dict, key=sort_key, reverse=True)
    return(list_dict[0:nr])
    
    # These "asserts" using for self-checking and not for auto-testing
assert bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]) == [
    {"name": "wine", "price": 138},
    {"name": "bread", "price": 100}
], "First"

assert bigger_price(1, [
    {"name": "pen", "price": 5},
    {"name": "whiteboard", "price": 170}
]) == [{"name": "whiteboard", "price": 170}], "Second"

print('Done! Looks like it is fine. Go and check it')



def bigger_price(limit, data):
    """
        TOP most expensive goods
    """
    # your code here
    return None


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')





#Your optional code here
#You can import some modules or create additional functions

lst = [1, 2, 3, 1, 3]
lst_dict = {}
for i in lst:
    if i in lst_dict:
        lst_dict[i]+=1
    else:
        lst_dict[i] = 1
for i in lst:
    if lst_dict[i] == 1:
        lst.remove(i)
return lst        
        
        
lst2 = []        
for key, value in lst_dict.items():
    if value > 1:
        lst2.append(key)
        



lijst = [1, 2, 3, 4, 5]
for i in lijst:
    if lijst.count(i) == 1:
        lijst.remove(i)
print(lijst)    

i  = 0
lijst = [1, 2, 3, 4, 5]
while i < len(lijst):
    print(lijst[i])
    i+=1




def checkio(lst: list) -> list:
    



def checkio(lst: list) -> list:
    lst_dict = {}
    for i in lst:
        if i in lst_dict:
            lst_dict[i]+=1
        else:
            lst_dict[i] = 1
    lst_copy = lst.copy()
    for i in lst_copy:
        if lst_dict[i] == 1:
            lst.remove(i)
    return lst      

checkio([1, 2, 3, 4, 5])


#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")



count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3

def count_word(zin, dicto):
    
zin =     "How aresjfhdskfhskd you?"
dicto = {"how", "are", "you", "hello"}

zin2 = zin.lower().split()
if dict[0] in zin2:
    print('yes')


# find block to check
for i in range(len(x[1]) -3):
    print(i)
    if x[i][i+1] == x[i][i+2] == x[i][i+3] == x[i][i+4]: 
        print("True ")
    else: 
        print("False")
     
        
       

m = [
        [1, 0, 0, 1, 1, 1],
        [1, 8, 7, 3, 1, 5],
        [0, 3, 3, 2, 5, 1],
        [0, 1, 1, 1, 1, 4],
        [0, 6, 5, 1, 1, 1],
        [0, 1, 9, 1, 2, 1]
    ]
      
def checkio(m):
    i = 0
    j = 0 
    squares = len(m[0])
    for i in range(squares):
        for j in range(squares):
            try:
                # dit is om rij te checken vanaf 0,0
                rij = m[i][j] == m[i][j+1] == m[i][j+2] == m[i][j+3]
                # dit is om kolom te checken vanaf 0,0
                kol =  m[i][j] == m[i+1][j] == m[i+2][j] == m[i+3][j]
                # dit is om diagonaal te checken vanaf 0,0
                dia =  m[i][j] == m[i+1][j+1] == m[i+2][j+2] == m[i+3][j+3]
                if rij or kol or dia:
                    return True
            except:
                pass
    return False


checkio(m)



squares = len(m[0]) - 3
for i in range(squares):
    for j in range(squares):
        print('i:', i, 'j:' ,j)
        # dit is om rij te checken vanaf 0,0
        print('rij: ', m[i][j] == m[i][j+1] == m[i][j+2] == m[i][j+3])
        
        # dit is om kolom te checken vanaf 0,0
        print('kol: ', m[i][j] == m[i+1][j] == m[i+2][j] == m[i+3][j])
        
        # dit is om diagonaal te checken vanaf 0,0
        print('dia: ', m[i][j] == m[i+1][j+1] == m[i+2][j+2] == m[i+3][j+3])


  
   


     
x[0][0]
x[0][1]
x[0][2]
x[0][3]
x[0][4]

x[0][0]
x[1][0]
x[2][0]
x[3][0]
x[4][0]






for i in range(len(x[1]) -3):
    print(i)
    if x[i+1][i] == x[i+2][i] == x[i+3][i] == x[i+4][i]: 
        print("True ")
    else: 
        print("False")

for i in range(1):
    print(i)

for rownum = 
x[2][0]


for i in x:
    print(len(i))
    



def checkio(m):
    i = 0
    j = 0 
    squares = len(m[0])
    for i in range(squares):
        for j in range(squares):
            try:
                # dit is om rij te checken vanaf 0,0
                rij = m[i][j] == m[i][j+1] == m[i][j+2] == m[i][j+3]
                # dit is om kolom te checken vanaf 0,0
                kol =  m[i][j] == m[i+1][j] == m[i+2][j] == m[i+3][j]
                # dit is om diagonaal ne-sw te checken vanaf 0,0
                dia_ne_sw =  m[i][j] == m[i+1][j+1] == m[i+2][j+2] == m[i+3][j+3]
                # dit is om diagonaal sw-ne te checken vanaf 0,0
                # dia_ne_sw =  m[i][j] == m[i-1][j-1] == m[i-2][j-2] == m[i-3][j-3]
                if rij or kol or dia_ne_sw: #or dia_ne_sw:
                    print("i:",i,"j:",j)
                    return True
            except:
                pass
    return False



#i = 0
#j = 0
#m[4][0]
#checkio(m)


def test_rij(m):
    size = len(m[0])
    i_range = size
    j_range = size - 3
    for i in range(i_range):
        for j in range(j_range):
            match = m[i][j] == m[i][j+1] == m[i][j+2] == m[i][j+3]
            if match:
                return True
                       
def test_kolom(m):
    size = len(m[0])
    i_range = size - 3
    j_range = size
    for i in range(i_range):
        for j in range(j_range):
            match = m[i][j] == m[i+1][j] == m[i+2][j] == m[i+3][j]
            if match:
                return True
                
def test_dia_nw_se(m):
    size = len(m[0])
    i_range = size - 3
    j_range = size - 3
    for i in range(i_range):
        for j in range(j_range):
            match = m[i][j] == m[i+1][j+1] == m[i+2][j+2] == m[i+3][j+3]
            if match:
                return True

def test_dia_sw_ne(m):
    size = len(m[0])
    i_range = size - 3
    j_range = size - 3
    for i in range(i_range, size):
        for j in range(j_range):
            match = m[i][j] == m[i-1][j+1] == m[i-2][j+2] == m[i-3][j+3]
            if match:
                return True
            
def checkio(m):
    if test_rij(m) or test_kolom(m) or test_dia_nw_se(m) or test_dia_sw_ne(m):
        return True
    return False

def checkio(m):
    if test_rij(m): return True
    if test_kolom(m): return True
    if test_dia_nw_se(m): return True
    if test_dia_sw_ne(m): return True
    return False

checkio(m)    

checkio([[7,1,4,1],[1,2,5,2],[3,4,1,3],[1,1,8,1]])

m =  [
    [7,1,4,1],
    [1,2,1,2],
    [3,1,1,3],
    [1,1,8,1]] 
 
test_rij(m)
test_kolom(m)
print(test_dia_nw_se(m))
print(test_dia_sw_ne(m))
    
m = [
    [3, 9, 4, 5, 4, 1],
    [1, 1, 5, 4, 1, 8],
    [9, 5, 1, 2, 1, 9],
    [5, 9, 8, 1, 9, 4],
    [5, 6, 1, 9, 1, 1],
    [5, 1, 9, 9, 9, 1]
]
                

checkio(m)

def checkio(expression):
    return True or False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

open_hooks = ["]",")"]



'['.find(str_types)
str_types.find('[')

str_types = '()[]{}'
x = "[1+1]+(2*2)-{3/3}"
open_hooks = []
for i in x:
    if i in ("[","{","("):
        open_hooks.append(str_types.find(i))
    if i in ("]","}",")"):
        if open_hooks[-1] == open_hooks[str_types.find(i)-1]:
            print('this matches')
            del open_hooks[-1]
        else:
            print('this sucks')



goal = 56
big = 10
small = 6
def tst (goal, big, small):
    return  goal % big <= small if big > 0 else False

tst(goal, big, small)



import functools

def checkio(number):
    """
    Return the smallest integer such that the product of its digits equal 'number'.
    If this is not possible, return zero.
    """
    # Special case for one to keep the logic simpler (and zero, as an early out).
    if number <= 1:
        return number

    # Factor number into factors in the range [2, 9] (inclusive)
    factors = []
    for d in reversed(range(2, 10)):
        while number > 1 and not number % d:
            number //= d
            factors.append(d)
            
    # If the number has not been completely factored, it must have prime
    # factors larger than seven.  In this case, it's impossible to factor
    # with digits, so return zero.
    if number > 1:
        return 0
    
    # Combine the factors back into a single integer.
    # Use reversed so that smaller digits come first.
    return functools.reduce(lambda a, b: 10 * a + b, reversed(factors))

checkio(100)

if __name__ == '__main__':
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(5) == 5, "5th example"




number = 40
d = 8
number // d
not number % d

divisor = []
for d in reversed(range(2,10)):
    if number % d == 0:
        divisor.append(d)
        break
divisor

for d in range(9,1,-1):
    print(d)
    
for d in reversed(range(2,10)):
    print(d)
    
def biggest_divisor(number):
    for d in range(9,1,-1):
        if number % d == 0:
            if number / d > 9:
                again = True
            else:
                again = False
            return (d, again, int(number / d))
    return(0, False, 0)


def checkio_j(number):
    again = True
    list_int = []
    while again:
        int_append, again, last_num = biggest_divisor(number)
        list_int.append(int_append)
        if again:
            number = number / list_int[-1]
    if list_int !=0:
        list_int.append()
    return list_int

biggest_divisor(20)

n=13
checkio(n)
checkio_j(n)

print(biggest_divisor(100))
print(biggest_divisor(20))
print(biggest_divisor(125))
print(biggest_divisor(25))
print(biggest_divisor(9))

def biggest_divisor(number):
    for d in range(9,1,-1):
        if number % d == 0:
            return (d, int(number / d))
    return(0, 0)

biggest_divisor(20)


def checkio_j(number):
    list_int = []
    remainder = 10
    while remainder > 9:
        int_append, remainder = biggest_divisor(number)
        list_int.append(int_append)
        number //= 
        if number < 10:
            list_int.append(number)
    if list_int !=0:
        list_int.append()
    return list_int

biggest_divisor(25)

n=125
checkio(n)
biggest_divisor(n)
checkio_j(n)

print(biggest_divisor(100))
print(biggest_divisor(20))
print(biggest_divisor(125))
print(biggest_divisor(25))
print(biggest_divisor(9))

while True:
    for i in ["/","-" ,"|","\\","|"]:
        print ("%s\r" % i,)
        
        
def checkio(first, second):
    return ""

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"




first = "one,two,three"
second = "four,five,one,two,six,three"

match = []
for w1 in first.split(','):
    for w2 in second.split(','):
        if w1 == w2:
            match.append(w1)
print(",".join(match))

test = ""
for i in first:
    test.join(i)
print(test)




music = ["Metallica", "John", "Frusciatne"]
type(music)
print (",".join(music))



def checkio(first,second):
    match = []
    for w1 in first.split(','):
        for w2 in second.split(','):
            if w1 == w2:
                match.append(w1)
    match.sort()
    return(",".join(match))

print(checkio(first,second))

print(match.sort())
print(match)        


 x= [
"..O",
"X.O",
"OXO"]

def checkio(x):
    for i in range(3):
        t1 = {x[i][0], x[i][1], x[i][2]}
        t2 = {x[0][i], x[1][i], x[2][i]}
        if len(t1) == 1 and '.' not in t1:
            return(t1.pop())
        elif len(t2) == 1 and '.' not in t2:
            return(t2.pop())
    t3 =   {x[0][0], x[1][1], x[2][2]}
    t4 =   {x[2][0], x[1][1], x[0][2]}
    if len(t3) == 1 and '.' not in t3:
        return(t3.pop())
    if len(t4) == 1 and '.' not in t4:
        return(t4.pop())
    return "D"

def checkio(res: List[str]) -> str:
    a = [res[n][n] for n in range(len(res)) if res[n][0] == res[n][1] == res[n][2] != "." or res[0][n] == res[1][n] == res[2][n] != "."]
    if a:
        return a[0]
    if res[0][0] == res[1][1] == res[2][2] != "." or res[2][0] == res[1][1] == res[0][2] != ".":
        return res[1][1]
    return "D"


checkio(x)


def checkio(x):
    pass

checkio([1, 2, 3, 4, 5]) == 3
checkio([3, 1, 2, 5, 3]) == 3
checkio([1, 300, 2, 200, 1]) == 2
checkio([3, 6, 20, 99, 10, 15]) == 12.5

x = [3, 6, 20, 21]

def checkio(x):
    x=sorted(x)
    if len(x)%2 == 1:
        return(x[int(len(x)/2-0.5)])
    else:
        tel = len(x)/2
        return((x[int(tel)-1] + x[int(tel)])/2)

  def checkio2(data):
    data = sorted(data)
    i = int((len(data) - 1)/2)
    return data[i] if len(data) % 2 else ((data[i] + data[i+1])/2)


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


def get_word_value(word):
    value = 0
    for i in word:
        value += int(letter_dict[i])
    return value
    
def most_valuable_word(words):
    max_value = 0
    max_value_word = ''
    for word in words:
        if get_word_value(word) > max_value:
            max_value_word = word
            max_value =  get_word_value(word)
    return max_value_word


summ = sum(letter_dict[j] for  word in words)





















