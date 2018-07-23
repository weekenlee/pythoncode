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
