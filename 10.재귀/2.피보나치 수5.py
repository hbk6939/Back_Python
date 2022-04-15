from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())

def Fibo_num(x :int) -> int:
    if x>=2:
        return Fibo_num(x-1) + Fibo_num(x-2)
    elif x == 1:
        return 1
    else:
        return 0

def Fibo_num2(x :int, before=0, after=1) -> int:
    if x>=2:
        return Fibo_num2(x-1, after, before+after)
    elif x == 1:
        return after
    else:
        return 0

print(Fibo_num(n))
print(Fibo_num2(n))