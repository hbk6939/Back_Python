from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

ls = [int(si.readline()) for i in range(28) ]

cmp = [i for i in range(1,31)]
res = []

for i in cmp:
    if i not in ls:
        res.append(i)
print(min(res))
print(max(res))


