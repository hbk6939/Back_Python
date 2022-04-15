from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())

def sum_of(x :int) -> int:
    x = sum( map(int, str(x) ) ) + x
    return x

res = 0

for i in range(n):
    if sum_of(i) == n:
        res = i
        break

if res == 0:
    so.write(f"{0}")
else:
    so.write(f"{i}")