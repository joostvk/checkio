def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    frq_dict = {}
    for lt in data:
        if lt not in frq_dict:
            frq_dict[lt] = 1
        else:
            frq_dict[lt] += 1   
    max_val = max(frq_dict.values())
    for key, value in frq_dict.items():
        if value == max_val:
            max_key = key
    return max_key

# faster solution on checkio
def most_frequent2(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    return max(set(data), key=data.count)

# paar probeerseltjes
data =['a', 'a', 'b', 'b']
x= set(data)
type(x)

y = {'a','b','a','c'}
print(data.count)
