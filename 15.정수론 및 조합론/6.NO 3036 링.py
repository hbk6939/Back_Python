from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

def GCD(x, y): # 유클리드 호제법으로 최대공약수
    while y:
        x, y = y, x%y
    return x
    


n = int(si.readline())
ls = list(map(int, si.readline().split()))
# print(ls)

for i in range(1, len(ls)):
    # print(f"ls[i]/ls[0] = {ls[0]}/{ls[i]} = {ls[0]/ls[i]}")
    gcd = GCD(ls[0], ls[i])
    # print(gcd)
    # print(f"ls[i]/ls[0] = {ls[0]//gcd}/{ls[i]//gcd}")
    so.write(f"{ls[0]//gcd}/{ls[i]//gcd}\n")