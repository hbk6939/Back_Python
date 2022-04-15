from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())

def Fib(a :int)->int:
    if a==0:return 0
    if a==1:return 1
    return Fib(a-1) + Fib(a-2)        

print(Fib(n))