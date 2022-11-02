from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")
ls = []
num_Max = float('-inf')
idx = ''

for i in range(9):
    ls.append(list(map(int, si.readline().split())))
    for j in range(9):
        if ls[i][j] > num_Max:
            num_Max = ls[i][j]
            idx = f"{i+1} {j+1}"

print(num_Max)
print(idx)