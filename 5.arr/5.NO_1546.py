from sys import stdin as si, stdout as so

n = int(si.readline())
ls = list(map(int, si.readline().strip().split()))

m = max(ls)

ls = [ls[i]/m*100 for i in range(n)]

print(sum(ls)/n)