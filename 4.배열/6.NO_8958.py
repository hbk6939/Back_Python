from sys import stdin as si, stdout as so

n = int(si.readline())
ls = [si.readline().strip() for _ in range(n)]

for i in ls:
    score = 0
    cum = 0

    for j in i:
        # so.write(f"{j} ")
        if j == "O":
            cum += 1
            score += cum
        elif j == "X":
            cum = 0
            
    so.write(f"{score}\n")