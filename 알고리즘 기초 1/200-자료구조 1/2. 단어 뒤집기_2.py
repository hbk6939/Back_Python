from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())

for i in range(n):
    ls = si.readline().split()
    for j in ls:
        so.write(f"{j[::-1]} ")
    so.write("\n")