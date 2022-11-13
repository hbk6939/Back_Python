from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

N, K = map(int, si.readline().split())

son = 1; mom = 1
for i in range(K):
    son *= N-i
    mom *= K-i
    # so.write(f"(N-i)/(K-i) : {son}/{(mom)} = {(son)/(mom)}\n")
print(son/mom)