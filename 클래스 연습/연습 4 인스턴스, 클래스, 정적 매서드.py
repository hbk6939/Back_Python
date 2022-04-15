class foo:
    a = 0                               # class member

    def instance_method(self):
        self.b = 10                     # instance member
        print("instance method called")
        return self.b

    @classmethod
    def class_method(cls):
        print("class method called")
        cls.a = 20
        return cls.a                    # class member에 접근 가능

    @staticmethod
    def static_method():
        print("static method called")

f = foo()
print("1. f.instance_method()------------------------")
print(f.instance_method())
print(f"클래스 변수 a : {f.a}")
print("2. f.class_method()------------------------")
print(f.class_method())
print(f"클래스 변수 a : {f.a}")
print("3. f.static_method()------------------------")
print(f.static_method())
print(f"클래스 변수 a : {f.a}")
print("4. foo.static_method()------------------------")
print(foo.static_method())
print(f"클래스 변수 a : {f.a}")
