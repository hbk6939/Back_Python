from sys import stdin as si, stdout as so

t = int(si.readline())

# a층의 b호에 살려면 자신의 아래(a-1)층의 
# 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다

ls = [[0]*15 for i in range(15)]

# 0층 0~14, 1호 == 1
for i in range(15):
    ls[0][i] = i
    ls[i][1] = 1

for i in range(1, 15): # 층
    for j in range(2, 15): #호
        ls[i][j] = ls[i-1][j] + ls[i][j-1]

# for i in range(14,-1,-1): # 확인
#     print(ls[i])

for i in range(t):
    a = int(si.readline()) # 0층 ~
    b = int(si.readline()) # 1호 ~
    so.write(f"{ls[a][b]}\n")
