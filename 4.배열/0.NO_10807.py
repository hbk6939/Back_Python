from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개

N = int(si.readline())
ls = list(map(int, si.readline().split()))
v = int(si.readline())
# N = int(input())
# ls = list(map(int, input().split()))
# v = int(input())

cnt = 0
for i in range(N):
    if ls[i] == v:
        cnt+=1

print(cnt)