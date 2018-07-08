cipher_grille =       (
'X...' ,
'..X.' ,
'X..X' ,
'....' )

letters = ('itdf',
         'gdce',
         'aton',
         'qrdi')


coordinates = []
len_cipher_grille = len(cipher_grille)
# loop through cipher_grill and store coordinates of X's
for i in range(len_cipher_grille):
    for j in range(len_cipher_grille):
        if cipher_grille[i][j] == 'X':
            coordinates.append((i,j))
            
password  = ''
for x,y in coordinates:
    password.append((letters[x][y]))

tst = 'joost'
tst.
tst.append('jj')
tst

grille = list((y, 3 - x) for (x, y) in coordinates)

for x,y in coordinates:
    print(letters[x][y])

# find letters on coordinates
letters[0][0]


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


names = [('joost',1974), ('janneke',1976), ('lena',2007), ('daniel',2011)]
x = [(name, jaar) for (name,jaar) in names if jaar > 2000]
x
