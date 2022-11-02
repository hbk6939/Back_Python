from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())
ls = [si.readline().strip().split() for _ in range(n)]
for i in range(len(ls)):
    ls[i][0] = int(ls[i][0])
    ls[i].append(i)

# print(ls)

ls.sort(key = lambda x : (x[0], x[2]))
# so.write("\n".join(ls))
[so.write(f"{ls[i][0]} {ls[i][1]}\n") for i in range(len(ls))]
# [so.write(f"{ls[i]}\n") for i in range(len(ls))]
