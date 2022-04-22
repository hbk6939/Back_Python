from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())
ls = [list(si.readline().split()) for _ in range(n)]

for i in ls:
    for b in i:
        so.write(f"{b[::-1]} ")
    so.write("\n")