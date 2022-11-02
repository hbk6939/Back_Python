from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())
res = 1
while n!=1:
    res *= n
    n -= 1
    # print(f"before*{n}={res}")

print(res)