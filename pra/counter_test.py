import collections

print(collections.Counter(['a', 'b', 'c', 'a']))
print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))
print(collections.Counter(a=2, b=3, c=1))

c = collections.Counter()
print('Initial:', c)

c.update('abcdaab')
print('Sequence:', c)

c.update({'a': 1, 'd': 5})
print('Dict :', c)

for letter in 'abcde':
    print('{}: {}'.format(letter, c[letter]))

print(list(c.elements()))

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabert')
print("math.....")
print(c1)
print(c2)
print(c1+c2)
print(c1-c2)
print(c1 & c2)
print(c1 | c2)
