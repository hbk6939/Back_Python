from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())
row_ls = list(map(int, si.readline().split()))

sorted_ls = sorted(set(row_ls))
# print(sorted_ls)
dic = {}

for i in range(len(sorted_ls)):
    dic[sorted_ls[i]] = i
# print(dic)

for i in range(n):
    so.write(f"{dic[row_ls[i]]} ")