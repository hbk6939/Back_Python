from sys import stdin as si, stdout as so

# 입력
n = int(si.readline())

def nextNum(x):
    n10 = x//10 # 주어진 수의 왼쪽 자리
    n1 = x%10 # 주어진 수의 오른쪽 자리
    sumOfNum = n10 + n1
    sn1 = sumOfNum%10 # 더한 수의 오른쪽 자리
    return int(str(n1) + str(sn1))

cmp_n = n
cnt = 0

while True:
    cmp_n = nextNum(cmp_n)
    cnt += 1
    # print(cmp_n)
    if cmp_n == n:
        break

print(cnt)