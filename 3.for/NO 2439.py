from sys import stdin as si, stdout as so

n = int(si.readline())

for i in range(1, n+1):
    so.write(f"{' '*(n-i) + '*'*i}\n")
