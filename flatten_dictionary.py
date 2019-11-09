D = {"sleutel1": {"deeper": {"more": {"enough": "value"}}}, 'joost':'1234', 'janneke' : {'kind1':'Lena', 'kind2':'Daniel'}}

def depth(d, level=1):
    if not isinstance(d, dict) or not d:
        return level
    return (depth(d[k], level + 1) for k in d)

list(depth(d))

isinstance(test,dict)
for k in d:
    print(k)
d['key']



def go_deeper(wb):
    

for key in d:
    print(isinstance(d[key],dict))
    
def flatten(D, path=[]):
    if isinstance(D, dict):
        res = {}
        for key, val in D.items(): 
            res.update(flatten(val, path + [key]))
        return res
    if isinstance(D, str): 
        return {"/".join(path): D}    

flatten(D)

for key, val in D.items():
     print(key)
