class foo:
    count_of_instance = 0

    def __init__(self):
        foo.count_of_instance += 1

    def __del__(self):
        foo.count_of_instance -= 1

f1 = foo() # +=1
f2 = foo() # +=1
f3 = foo() # +=1
print(foo.count_of_instance)    # 3
del f2 # -=1
print(foo.count_of_instance)    # 2
del f3 # -=1
print(foo.count_of_instance)    # 1