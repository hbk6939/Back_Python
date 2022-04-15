from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())
ls = [si.readline().strip() for _ in range(n)]

ls = list(set(ls))
ls.sort(key = lambda x : (len(x), x))
# [so.write(f"{ls[i]}\n") for i in range(len(ls))]
so.write("\n".join(ls))