from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

total = int(si.readline())
tpyes = int(si.readline())
res = 0

for i in range(tpyes):
    ls = list(map(int, si.readline().split()))
    res += ls[0] * ls[1]

if res == total:
    print('Yes')
else:
    print('No')
