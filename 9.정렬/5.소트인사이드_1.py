from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

cnt = [0]*11
n = list(map(int, list(si.readline().strip())))

for i in range(len(n)):
    cnt[n[i]] += 1

for i in range(10, -1, -1):
    for j in range(cnt[i]):
        so.write(f"{i}")