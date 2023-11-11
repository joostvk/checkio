import itertools

def create_dict_from_list(circles):
    dct = {}
    for count, circle in enumerate(circles):
        circle_x = circle[0]
        circle_y = circle[1]
        circle_step = circle[2]
        dct[count] = [[circle_x - circle_step, circle_y - circle_step], [circle_x + circle_step,circle_y + circle_step]]
    return dct

def comp_cirles(dct1, dct2):
    ref_top = dct1[1][1]
    ref_left = dct1[0][0]
    ref_bot = dct1[0][1]
    ref_right = dct1[1][0]
    comp_top = dct2[1][1]
    comp_left = dct2[0][0]
    comp_bot = dct2[0][1]
    comp_right = dct2[1][0]
    if ref_top <= comp_bot or ref_left >= comp_right or ref_bot >=comp_top or ref_right <= comp_left:
        return 1
    else:
        return 0


def count_chains(circles):
    dct = create_dict_from_list(circles)
    print(dct)
    loose_cirle = 0
    single_square_dict = {}
    for i in itertools.combinations(range(len(dct)),2):
        loose_cirle = comp_cirles(dct[i[0]], dct[i[1]])
        if loose_cirle:
            cirle_ref = [i][0][0]
            single_square_dict[cirle_ref] = 1
    return sum(list(single_square_dict.keys()))

'hmmm die 4e gaat ie nu niet vergelijken, dat zuigt'


count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)])
count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2
count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1
count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4


