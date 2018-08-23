sq11 = [[1,2],[2,6],[5,6],[1,5]]
sq12 = [[2,3],[3,7],[6,7],[2,6]]


def checkio(lines):
    points = ([1, 2, 3, 5, 6, 7, 9, 10, 11], [1, 2, 5, 6], [1])
    lines = [set(line) for line in lines]

    def has_square(start, n):
        for off in 1, 4, -1, -4:
            for step in range(n):
                if {start, start + off} not in lines:
                    return False
                start += off
        return True

    return sum(has_square(p, n+1) for n in range(3) for p in points[n])


lines = [[1, 2], [1, 5], [2, 6], [5, 6]]
points = ([1, 2, 3, 5, 6, 7, 9, 10, 11], [1, 2, 5, 6], [1])
lines = [set(line) for line in lines]








width = 4
start = 1
ret = []
for i in range(width):
    ret.append([start + i, start + i + 1])
    ret.append([start + 4 * width + i, start + 4 * width + i + 1])
    ret.append([start + 4 * i, start + 4 * i + 4])
    ret.append([start + width + 4 * i, start + width + 4 * i + 4])
ret



for x in range(1,4):
    print(x)

first_name = 'joost'
last_name = 'van kruijsdijk'
sentence = 'my name is {} {}'.format(first_name, last_name)
print(sentence)

sentence = f'my name is {first_name} {last_name}'
print(sentence)


sentence = f'my name is {first_name.upper()} {last_name}'
print(sentence)


person = {'name':'joost', 'age':44}
sentence = 'my name is {} and i\'m {} years old'.format(person['name'],44)
print(sentence)

# with a format string
sentence=f"my name is {person['name']} and i am {person['age']} years old"
print(sentence)
