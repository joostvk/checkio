def checkio(num):
    """
    returns the number of 1's when a number is binary expressed
    """
    return bin(num).count('1')

checkio(4) 

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9



