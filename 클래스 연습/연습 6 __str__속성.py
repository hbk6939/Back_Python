class foo:
    pass

f = foo()
print(f)        # <__main__.goo object at 0x007324D0>
print(foo)
print(foo())
print()

class goo:
    def __str__(self):
        return "__str__이 오버라이딩 되었습니다."

g = goo()
print(g)        # __str__이 오버라이딩 되었습니다.
print()

print(goo)
print(goo())