import string

value = {'var': 'foo'}

t = string.Template("""
        Variable            :$var
        Escape              :$$
        Variable in text    :${var}iable
        """)

s = """
        Variable            :%(var)s
        Escape              :%%
        Variable in text    :%(var)siable
    """

s2 = """
        Variable            :{var}
        Escape              :{{}}
        Variable in text    :{var}siable
    """

print('Template:', t.substitute(value))
print('INTERPOLATION:', s % value)
print('FORMAT:', s2.format(**value))
