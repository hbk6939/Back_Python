from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

square = [[0]*100 for _ in range(100)]
n = int(si.readline())
for i in range(n):
    a, b = map(int, si.readline().split())
    for row in range(10):
        for col in range(10):
            square[a+row][b+col] = 1

cnt = 0
for i in square:
    cnt += sum(i)
print(cnt)

# print(sum(map(sum, square)))