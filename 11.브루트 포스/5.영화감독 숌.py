from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())
first = 666
cnt = 0

while True:
    if "666" in str(first):
        cnt+=1
    if cnt == n:
        print(first)
        break
    first += 1
    