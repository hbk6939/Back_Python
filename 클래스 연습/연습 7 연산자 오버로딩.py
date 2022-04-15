class MyOperator:
    def __mul__(self, i):
        self.a = 5
        return self.a + i

s = MyOperator()
print(s.__mul__(1))
print(s*10)       # 15

# print(s * 10)