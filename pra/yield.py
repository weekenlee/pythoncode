
def foo():
    while True:
        x = yield
        print(x)

if __name__=="__main__":
    f = foo()
    next(f)
    f.send(1)
    f.send(2)
    next(f)
