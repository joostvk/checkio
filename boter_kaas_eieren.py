from typing import List

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

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

