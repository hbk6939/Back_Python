from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())

def facto(x :int, res = 1) -> int:    
    if x == 1:
        return res
    if x==0:
        return 1
    return facto(x-1, res=res*x)
    

print(facto(n))