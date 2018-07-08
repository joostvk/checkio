cipher_grille =       (
'X...' ,
'..X.' ,
'X..X' ,
'....' )

letters = ('itdf',
         'gdce',
         'aton',
         'qrdi')


def recall_password(cipher_grille, letters):
    coordinates = []
    len_cipher_grille = len(cipher_grille)
    # loop through cipher_grill and store coordinates of X's
    for i in range(len_cipher_grille):
        for j in range(len_cipher_grille):
            if cipher_grille[i][j] == 'X':
                coordinates.append((i,j))
                
    password  = ''
    for x,y in coordinates:
        password = password + letters[x][y]
    
    for i in range(3):
        coordinates = sorted((y, 3 - x) for (x, y) in coordinates)
        for x,y in coordinates:
            password = password + letters[x][y]
    
    return password
