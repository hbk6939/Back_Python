from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())


for i in range(2, int(n**0.5)+1):
    while n%i == 0:
        so.write(f"{i}\n")
        n /= i

if n != 1:
    so.write(f"{int(n)}\n")