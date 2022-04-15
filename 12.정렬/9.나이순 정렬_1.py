from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())
ls = [si.readline().strip().split() for i in range(n)]
for i in range(n):
    ls[i][0] = int(ls[i][0])

ls.sort(key = lambda x : x[0])
[so.write(f"{ls[i][0]} {ls[i][1]}\n") for i in range(len(ls))]