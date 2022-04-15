from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = list(si.readline().strip())
n.sort(reverse=True)
[so.write(i) for i in n]