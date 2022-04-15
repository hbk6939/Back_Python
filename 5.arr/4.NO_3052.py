from sys import stdin as si, stdout as so

ls = [int(si.readline())%42 for _ in range(10)]
# print(ls)

cnt = 0

for i in range(42):
    if ls.count(i) > 0:
        cnt += 1

print(cnt)