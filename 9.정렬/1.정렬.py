from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())
ls = [int(si.readline()) for i in range(n)]

# [so.write(f"{i}\n") for i in sorted(ls)]

ls.sort()
[so.write(f"{i}\n") for i in ls]