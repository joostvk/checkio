def count_consecutive_summers(num):
    con_num = 1
    for i in range(1,num):
        counter = 0
        tot = i
        while tot <= num:
            counter += 1
            tot = tot + i +counter
            if tot == num:
               con_num += 1
    return con_num


count_consecutive_summers(99)





# start met een nummer in reeks
# test of nummer gelijk is aan raadnummer
# voeg volgende nummer toe aan reeks
        


     
        