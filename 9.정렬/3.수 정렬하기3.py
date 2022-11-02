from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())
cnt = [0 for _ in range(10001)]

# 나온 숫자의 갯수만큼 인덱스에 +1
for i in range(n):
    cnt[int(si.readline())] += 1

# print()
for i in range(10001):
    for j in range(cnt[i]):
        so.write(f"{i}\n")