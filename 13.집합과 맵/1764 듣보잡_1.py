from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")
# from collections import Counter

N, M = map(int, si.readline().split())
hear, see = set(), set()

for i in range(N):
    hear.add(si.readline().strip())
for i in range(M):
    see.add(si.readline().strip())

subset = hear&see
subset_ls = sorted(subset)
print(len(subset_ls))
print('\n'.join(subset_ls))