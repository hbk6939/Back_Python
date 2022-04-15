from sys import stdin as si, stdout as so

# 정수 N개 중 X보다 작은수
N, X = map(int, si.readline().split())
ls = list(map(int, si.readline().split()))

for i in ls:
    if i<X:
        so.write(f'{i} ')