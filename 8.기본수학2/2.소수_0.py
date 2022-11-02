import math
from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

a = int(si.readline()) # a <= b
b = int(si.readline())

def is_prime(n: int) -> bool:
    if n == 1:
        return False
        
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def add_prime_in_range(a: int, b: int)->int:
    res = 0
    for i in range(a, b+1):
        if is_prime(i):
            res += i
    return res

def first_prime(a: int, b: int)->int:
    for i in range(a, b+1):
        if is_prime(i):
            return i

x = add_prime_in_range(a, b)

if x == 0:
    print(-1)
else:
    print(x)
    print(first_prime(a,b))