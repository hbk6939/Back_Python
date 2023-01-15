from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")
def GCD(x:int, y:int)->int: # 최대공약수
    while y>0:
        x, y = y, x%y
    return x

ls = []
for i in range(int(si.readline())):
    ls.append(int(si.readline()))

gcdVal = abs(ls[0]-ls[1])

for i in range(2, len(ls)): # 차이값 끼리의 최대공약수
    gcdVal = GCD(gcdVal, abs(ls[i]-ls[i-1]))
    
arr = []
for i in range(2, int(gcdVal**0.5+1)):
    if i*i == gcdVal:
        arr.append(i)
    elif gcdVal%i == 0:
        arr.append(i)
        arr.append(gcdVal//i)
arr.append(gcdVal)
arr = sorted(arr)

print(*arr)
# print(' '.join(map(str, arr)))