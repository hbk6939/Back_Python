from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())

ls = [list(map(int, si.readline().split())) for _ in range(n)]

for i in range(n):
    rank = 1

    for j in range(n):
        if i==j:
            continue
        if ls[i][0] < ls[j][0] and ls[i][1] < ls[j][1]:
            rank += 1
    so.write(f"{rank} ")
            
    
        
        




