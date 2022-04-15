from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())

def sum_of(x :int) -> int:
    st = list( map(int, [i for i in str(x)] ) )
    for i in st:
        x += i
    return x # 


for i in range(n):
    if sum_of(i) == n:
        so.write(f"{i}")
        break
    if i == n-1:
        so.write(f"{0}")
