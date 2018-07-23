import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
c = {'c': 'E'}

m1 = collections.ChainMap(a, b)
print(m1)
print(m1['c'])

m2 = m1.new_child(c)
print(m1['c'])
print(m2['c'])
print(m2)
