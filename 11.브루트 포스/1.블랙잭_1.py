from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

# n: 카드의 개수, m: m을넘지 않아야함
n, m = map(int, si.readline().split())
ls = list(map(int, si.readline().split()))

res = 0
arr = []

# 카드 3개의 합 <= m 중 최대값
for i in range(n):
    for j in range(n):
        if i == j: continue
        
        for k in range(n):
            if j == k or i == k: continue
                
            res = ls[i] + ls[j] + ls[k]
            if res <= m:
                arr.append(res)

# so.write(f"{sorted(arr)}\n")
# so.write(f"{len(arr)}\n")
so.write(f"{max(arr)}\n")

