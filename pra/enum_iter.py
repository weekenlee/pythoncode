import enum

class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    wont_fix = 4

for status in BugStatus:
    print('{:15} ={}'.format(status.name, status.value))
