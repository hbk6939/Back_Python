from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

a, b = map(int, si.readline().split())

def Eratosthenes(a :int, b :int) -> list:
    # True = 소수 , False = 소수아님 
    ls = [True]*(b+1)

    for i in range(2, int(b**0.5)+1):
        if ls[i]:
            for j in range(2*i, b+1, i):
                ls[j] = False

            # j = 2
            # while i*j <= b:
            #     ls[i*j] = False
            #     j += 1
                
    ls[:2] = False, False
    ls[:a] = [False]*a
    return ls

ls = Eratosthenes(a,b)

for i in range(a, b+1):
    if ls[i]:
        so.write(f"{i}\n")
