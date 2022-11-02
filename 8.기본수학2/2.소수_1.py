from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

a = int(si.readline()) # a <= b
b = int(si.readline())

def is_prime(a :int, b :int):
    arr = [i for i in range(b+1)]
    arr[0:a] = [0]*a
    arr[:2] = 0,0

    for i in range(2, int(b**0.5)+1 ):
        j = 2

        while i*j <= b:
            arr[i*j] = 0
            j += 1
    return arr

def not_0(ls :list):
    for i in range(len(ls)):
        if ls[i] != 0:
            return i
    return -1

first_prime = not_0(is_prime(a, b))
sum_of_ls = sum(is_prime(a, b))

if first_prime == -1:
    print(-1)
else:
    print(sum_of_ls)
    print(first_prime)