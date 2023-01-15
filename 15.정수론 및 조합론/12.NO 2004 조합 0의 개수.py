from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

# nCm 의 끝자리 $0$의 개수를 출력하는 프로그램을 작성하시오.
n, m = map(int, si.readline().split())

def x_power_n(n, x):
    cnt=0
    while n>0:
        cnt += n//x
        n //= x
    return cnt

five = x_power_n(n, 5) - x_power_n(n-m, 5) - x_power_n(m, 5)
two = x_power_n(n, 2) - x_power_n(n-m, 2) - x_power_n(m, 2)
print(min(five, two))