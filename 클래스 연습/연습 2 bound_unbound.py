class Point:
    # Point 클래스의 setter , getter
    def set_x(self, x):
        self.x = x    # 인스턴스 멤버

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y    # 인스턴스 멤버

    def get_y(self):
        return self.y


# class를 통해 메서드 호출 ( unbound 방식 )
def unbound_class_call():
    p = Point()
    Point.set_x(p, 100)
    Point.set_y(p, 200)
    print(Point.get_x(p), Point.get_y(p))

def bound_instance_call():
    p = Point()
    p.set_x(10)
    p.set_y(20)
    print(p.get_x(), p.get_y())

print("unbound_class_call()")
unbound_class_call()
print("bound_instance_call()")
bound_instance_call()