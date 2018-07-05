import re


def test_patterns(text, patterns):
    for pattern, desc in patterns:
        print("{} ({})".format(pattern, desc))
        print(" '{} '".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.'*(s+n_backslashes)
            print("{} '{}'".format(prefix, substr))
        print()
    return


if __name__ == "__main__":
    test_patterns('abbaaaabababababa', [('ab', "'a' followed by b")])
