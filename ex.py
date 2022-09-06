from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

ls = list(map(int, si.readline().split()))
com = [1, 1, 2, 2, 2, 8]
res = []
for i, v in enumerate(ls):
     res.append(com[i] - v)

print(*res, sep=' ')

# res = map(str, res)
# print(' '.join(res))