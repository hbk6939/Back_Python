from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

# n: 카드의 개수, m: m을넘지 않아야함
n, m = map(int, si.readline().split())
ls = list(map(int, si.readline().split()))

res = 0
all_set = set()

# 카드 3개의 합 <= m 중 최대값
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            res = ls[i] + ls[j] + ls[k]
            
            if res <= m:
                all_set.add(res)

# so.write(f"{sorted(all_set)}\n")
# so.write(f"{len(all_set)}\n")
so.write(f"{max(all_set)}\n")

