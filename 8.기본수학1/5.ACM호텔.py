from sys import stdin as si, stdout as so

t = int(si.readline())

# 높이, 폭, 몇 번째 손님인지
for i in range(t):
    ls = list(map(int, si.readline().split()))

    front = (ls[2]%ls[0] if ls[2]%ls[0]!=0 else ls[0]) * 100
    back = (ls[2]//ls[0] + 1 if ls[2]%ls[0]!=0 else ls[2]//ls[0])

    so.write(f"{front+back}\n")
