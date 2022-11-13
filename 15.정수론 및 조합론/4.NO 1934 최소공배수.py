from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")
def GCD(x,y):
    while(y): #y가 참일 동안 = 자연수일 때 =   a%b!=0
        x,y=y,x%y
    return x

#최소공배수 구하기
def LCM(x,y):
    res = (x*y) // GCD(x,y)
    return res


T = int(si.readline())

for i in range(T):
    a, b = map(int, si.readline().split())
    so.write(f"{LCM(a, b)}\n")