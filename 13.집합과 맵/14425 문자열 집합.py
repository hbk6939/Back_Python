from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

N, M = map(int, si.readline().split())

N_set = set()
check = []

for i in range(N):
    N_set.add(si.readline().strip())

for i in range(M):
    check.append(si.readline().strip())

cnt = 0
for i in check:
    if i in N_set:
        cnt+=1
print(cnt)