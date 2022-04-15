from sys import stdin as si, stdout as so

n = int(si.readline())
ls = [list(map(int, si.readline().split())) for _ in range(n)]
# print(ls)

for i in ls:
    # print(i)
    avg = (sum(i) - i[0]) / i[0]
    # print("평균 :", avg)
    cnt = 0

    for j in range(1, i[0]+1):
        if i[j] > avg:
            cnt += 1
    so.write(f"{ round( (cnt/i[0])*100, 3 ):.3f}%\n")








