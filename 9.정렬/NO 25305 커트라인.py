from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

N, M = map(int, si.readline().split())
ls = list(map(int, si.readline().split()))

ls.sort(reverse=True)

print(ls[M-1])