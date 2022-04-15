from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

a, b = map(int, si.readline().split())
ls = [si.readline().strip() for _ in range(a)]
arr = []
    
for i in range(a-7):
    for j in range(b-7):
        cnt = 0
        compare = ls[0][0]
        for k in range(i, i+8):
            for l in range(j, j+8):
                if ls[k][l] != compare:
                    cnt +=1
                if compare == "B":
                    compare = "W"
                else:
                    compare = "B"
            if compare == "B":
                compare = "W"
            else:
                compare = "B"
        cnt = min(cnt, 64-cnt)
        arr.append(cnt)

print(min(arr))