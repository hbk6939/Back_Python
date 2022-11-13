from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

def nCk(N, K):
    son = 1; mom = 1
    for i in range(K):
        son *= N-i
        mom *= K-i
    return int(son/mom)

for i in range(int(si.readline())):
    a, b = map(int, si.readline().split())
    so.write(f"{nCk(b, a)}\n")