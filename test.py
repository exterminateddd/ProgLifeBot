def deco(func):
    def wrap(*args):
        func(*args)
    return wrap


@deco
def fn1(txt):
    print("some arged text: "+txt)


@deco
def fn2():
    print("some text")


fn1("tete")
