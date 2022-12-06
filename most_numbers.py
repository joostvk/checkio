
def checkio(*args):
    # for ar in args:
    #     print(ar)
    return max(args) - min(args) if len(args)> 0 else 0

checkio(1,2,3)


checkio(1, 2, 3) == 2
checkio(5, -5) == 10
checkio(10.2, -2.2, 0, 1.1, 0.5) == 12.4
checkio() == 0