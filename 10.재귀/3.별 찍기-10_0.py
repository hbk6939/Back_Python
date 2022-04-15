from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())
ls = [["*"]*n for _ in range(n)]

def star(a :int):
    div3 = a//3
    if div3 == 0:
        return
    # 중앙 공백
    
    
    for x in range(0, n, a):
        for y in range(0, n, a):
            for i in range(div3, div3*2):
                for j in range(div3, div3*2):
                    ls[i+x][j+y] = " "
    star(div3)

star(n)

for i in range(n):
    for j in range(n):
        so.write(f"{ls[i][j]}")
    so.write("\n")