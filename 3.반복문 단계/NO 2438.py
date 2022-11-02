from sys import stdin as si, stdout as so

n = int(si.readline())

for i in range(1, n+1):
    for j in range(i):
        so.write("*")
    so.write('\n')