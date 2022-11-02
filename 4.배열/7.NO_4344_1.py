from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())
ls = [list(map(int, si.readline().split())) for i in range(n)]


for i in ls:
    avg = sum(i[1:]) / i[0]
    
    cnt = 0
    for j in i[1:]:
        if j > avg:
            cnt+=1
    so.write(f"{round( (cnt/i[0])*100, 3 ):.3f}%\n")