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
    test_patterns('abbaaaabbababababa',
            [('ab*', "'a' followed by zero or more b"),
             ('ab+', "'a' followed by one or more b"),
             ('ab?', "'a' followed by zero or one b"),
             ('ab{3}', "'a' followed by three b"),
             ('ab{2,3}', "'a' followed by tow or three b"),
             ('ab{2,3}?', "'a' followed by tow or three b")]
            )
