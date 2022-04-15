from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())

arr = [-1]*(n+1)
arr[0] = 0
arr[1] = 1

def Fib(a :int)->int:
    if arr[a]==-1:
        arr[a] = Fib(a-1) + Fib(a-2)
    return arr[a]

print(Fib(n))