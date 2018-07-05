import re

text='abbaaabbbbaaaababababaadfda'

pattern = 'ab'

for match in re.findall(pattern, text):
    print('Found {!r}'.format(match))
