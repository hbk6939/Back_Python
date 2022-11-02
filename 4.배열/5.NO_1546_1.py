from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())
ls = list(map(int, si.readline().split()))

M = max(ls)
ls = [(i/M)*100 for i in ls]

print(sum(ls)/len(ls))