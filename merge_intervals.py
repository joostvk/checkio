def merge_intervals(orig):
    new = []
    temp_tup = orig[0]
    nr_tuples = len(orig)-1
    for i,j in enumerate(orig[0:nr_tuples]):
        if orig[i+1][0] > orig[i][1]:
            new.append(temp_tup)
            temp_tup = orig[i+1]
        else:
            temp_tup = (orig[i][0],max(orig[i][1],orig[i+1][1]))
            print(temp_tup)
            
    if orig[nr_tuples][0] > new[-1][1]:
        new.append(orig[nr_tuples])
    else:
        new[-1][1] = orig[-1][1]
    return new
        
  
merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)])
  