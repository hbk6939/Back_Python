from sys import stdin as si, stdout as so

# 정수 N개 중 X보다 작은수
N, X = map(int, si.readline().split())

for i in list(map(int, si.readline().split())):
    if i<X:
        so.write(f'{i} ')
