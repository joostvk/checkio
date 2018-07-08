cipher_grille =       (
'X...' ,
'..X.' ,
'X..X' ,
'....' )


letters = ('itdf',
         'gdce',
         'aton',
         'qrdi')

grille = sorted((x, y) for x in range(4) for y in range(4) if cipher_grille[x][y] == 'X')


x = ((x, y) for x in range(4) for y in range(4) if cipher_grille[x][y] == 'X')
x()

coordinates = []
len_cipher_grille = len(cipher_grille)
for i in range(len_cipher_grille):
    for j in range(len_cipher_grille):
        if cipher_grille[i][j] == 'X':
            coordinates.append((i,j))

grille = list((y, 3 - x) for (x, y) in coordinates)


git remote add origin git@github.com:joostvk/checkio.git
            
for x in coordinates:
    print(x)
            
            
            
grille2 = list((y, 3 - x) for (x, y) in grille)

coordinates
list(grille)


list(grille)
print(((y, 3 - x) for (x, y) in coordinates))


print((x,y) for (x,y) in coordinates)


for (x,y) in cipher_grille:
    print(x,y)
    
type(cipher_grille)


names = ['joost', 'janneke', 'lena', 'daniel']
x = [name for name in names if name[0].upper() == 'J']
x


names = [('joost',1974), ('janneke',1976), ('lena',2007), ('daniel',2011)]
x = [(name, jaar) for (name,jaar) in names if jaar > 2000]
x
