from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())

def sum_of(x :int) -> int:
    sum_each = 0 # 각 자릿수의 합
    num = x # 받은수
    while num > 0:
        sum_each += num%10
        num //= 10
    return sum_each + x

res = 0

for i in range(n):
    if sum_of(i) == n:
        res = i
        break

if res == 0:
    so.write(f"{0}")
else:
    so.write(f"{i}")