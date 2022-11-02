from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

N, M = map(int, si.readline().split())
ls = []
for i in range(N*2):
    ls.append(list(map(int, si.readline().split())))
# print(ls)

for i in range(N): # 행 길이 
    for j in range(M): # 열 길이
        so.write(f"{ls[i][j]+ls[i+N][j]} ") # i번째 행 + i+N(행 길이) 번째 행 끼리 더함
    so.write('\n')
