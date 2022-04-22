from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())

for i in range(n):
    ls = si.readline()[::-1].split()
    ls.reverse()
    so.write(" ".join(ls)+"\n")