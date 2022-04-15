class MyClass:
    def foo(self, x):
        print(x)

m = MyClass()
MyClass.foo(m, 20)      # 클래스 name sapce
m.foo(10)               # 객체 name space