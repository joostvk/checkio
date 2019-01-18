# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 21:16:59 2018

@author: JOOST
"""

nums = [1,2,3]

nums.__iter__()
print(dir(nums))
print(next(nums))

i_nums = nums.__iter__()
# is the same as
i_nums = iter(nums)

next(i_nums)
print(i_nums)

print(dir(i_nums))

sentence = ' joost is gek' 

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]

my_sentence = Sentence('Joost is gek' )
        
for word in my_sentence:
    print(word)        
    
def sentence(sentence):
    for word in sentence.split():
        yield word
        
my_sentence = sentence('Joost is gek' )
        
for word in my_sentence:
    print(word)

next(my_sentence)    



def outer_function(msg):
    message =  msg
    
    def inner_function():
        print(message)

    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()

# a decorator is a function that takes another function
# as an argument and adds some kind of function
# and returns this as a function


def decorator_function(message):
    def wrapper_function():
        print(message)
    return wrapper_function

hi_func = decorator_function('Hi')
bye_func = decorator_function('Bye')

hi_func()
bye_func()



def decorator_function(original_function):
    def wrapper_function():
       return original_function()
    return wrapper_function

hi_func = decorator_function('Hi')
bye_func = decorator_function('Bye')

hi_func()
bye_func()



def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,11):
    print(n, ":", fibonacci(n))

# memoization
    
fibonacci_cache = {}    

def fibonacci(n):
# if we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value =  1
    elif n == 2:
        value =  2
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = value
    return value


from functools import lru_cache
@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
 

 












































