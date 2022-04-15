from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

a, b = map(int, si.readline().split())

def is_prime(n :int) -> bool:
    if n == 0 or n == 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

for i in range(a, b+1):
    if is_prime(i):
        so.write(f"{i}\n")
