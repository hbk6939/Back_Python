from sys import stdin as si, stdout as so

ls = list(map(int, si.readline().split()))
print(ls)

def solve(a):
    x = 0
    for i in a:
        x += i
    return x

print(solve(ls))









