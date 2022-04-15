from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())
ls = [list(map(int, si.readline().split())) for _ in range(n)]

ls.sort(key = lambda x : (x[1], x[0])) # 튜플 원소앞에 '-'를 붙이면 내림차순
# print()
[so.write(f"{ls[i][0]} {ls[i][1]}\n") for i in range(n)]

