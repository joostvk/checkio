def checkio(lines_list):
    """Return the quantity of squares"""
    return 1


if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"

    
square1 = [[1,2],[2,6],[1,5],[5,6]]    
square2 = [[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]
                     
square1.sort(key=lambda x: x[0])
square1
square2.sort(key=lambda x: x[0])
square2



for i in range(1,15,1):
    square1[0][0] += i
    print(square1)
    
print(square1+1)

x = [[1,2],[2,6],[1,5],[5,6]] 
y = [[1,2],[2,6],[1,5],[5,6]]

sq = 0
for i in range(len(x)):
    if x[i] in y:
        print('y')
    else:
        print('n')
l1 = [(n, n + 4, n + 5, n + 1) for n in (1, 2, 3, 5, 6, 7, 9, 10, 11)]
l1



#anti-clock
#l1 = [(n, n + 4, n + 5, n + 1) for n in (1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15)]
l1 = [(n, n + 4, n + 5, n + 1) for n in (1, 2, 3, 5, 6, 7, 9, 10, 11)]
l2 = [(n, n + 4, n + 8, n + 9, n + 10, n + 6, n + 2, n + 1) for n in (1, 2, 5, 6)]
l3 = [(1, 5, 9, 13, 14, 15, 16, 12, 8, 4, 3, 2)]

#construct lines of squere 
def seg_gen(path):
    l = len(path)
    for i in range(l):
        yield sorted((path[i], path[(i + 1) % l])) #each time return a line of this squre

def checkio(lines_list):
    segments = [sorted(segment) for segment in lines_list] #segment is like this form [little, big]
    count = 0
    for square_list in (l1, l2, l3):
        for square in square_list:
            if all([seg in segments for seg in seg_gen(square)]): #if the square line all in given lines_list then that's a square
                count += 1

    return count


for square_list in (l1, l2, l3):
    for square in square_list:
        print(square)



path= (1, 5, 6, 2)
l = 1
sorted((path[i], path[(i + 1) % l]))

x =[1,3,7]
y = [1,3,7,9]

all([ for x in y])

z = [z**2 for z in x]
z



















