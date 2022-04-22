from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())
ls = [list(si.readline().split()) for _ in range(n)]

def reverse_one(s :str):
    res = ""
    for i in range(len(s)-1, -1, -1):
        res += s[i]
    return res

for i, j in enumerate(ls):
    for a in ls[i]:
        so.write(f"{reverse_one(a)} ")
    so.write("\n")