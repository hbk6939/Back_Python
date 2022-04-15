from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")


ls = [si.readline().split() for _ in range(3)]


# x축 y축중 처음 나온 값이 결과점
x = 0; y = 0

if ls[0][0] == ls[1][0]:
    x = ls[2][0]
elif ls[1][0] == ls[2][0]:
    x = ls[0][0]
else:
    x = ls[1][0]


if ls[0][1] == ls[1][1]:
    y = ls[2][1]
elif ls[1][1] == ls[2][1]:
    y = ls[0][1]
else:
    y = ls[1][1]

so.write(f"{x} {y}")


