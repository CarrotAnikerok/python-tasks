a_list = [10, "hello", 42.0, True]
a_set = {10, "hello", 42.0, True}
a_frozenset = frozenset(a_list)

def shrinkFrozenset(a):
    nset=set(a)
    lis=[i for i in a]
    if len(a)!=0:
        nset.remove(lis[0])
    nset=frozenset(nset)
    return nset

d = "Я гуляю в красоте ужаса миров"
print(" ".join(d))
print("стало", shrinkFrozenset(a_frozenset))
print("было", a_frozenset) 

