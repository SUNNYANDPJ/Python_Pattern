#coding: utf8


class Single(object):
    class _A(object):
        def __init__(self):
            pass

        def display(self):
            print id(self)

    _instance = None

    def __init__(self):
        if Single._instance is None:
            Single._instance = Single._A()

    def __getattr__(self, attr):
        return getattr(Single._instance, attr)


if __name__ == "__main__":
    a = Single()
    b = Single()
    print id(a), a.display()
    print id(b), b.display()

