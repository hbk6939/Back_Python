from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

# 빨간선 : 행성계 진입 이탈 최소화 경로
# 원 : 행성계 경계
# input
# 케이스수 T
# (출발점(x,y), 도착점(x,y))
# 행성계 개수 n
# n줄만큼 행성계 중점&반지름 (x,y,r)

# 출발, 도착점 1개만 속하면 cnt++

T = int(si.readline())

for i in range(T):
    x1, y1, x2, y2 = map(int, si.readline().split())
    n = int(si.readline())
    cnt = 0
    for i in range(n):
        x, y, r = map(int, si.readline().split())
        start = ((x1-x)**2 + (y1-y)**2)**0.5 # 행성 중심부터 시작점까지 거리
        end = ((x2-x)**2 + (y2-y)**2)**0.5 # 행성 중심부터 도착점 까지 거리
        # print(x,y,r)
        # print(f"({start}<{r}) ^ ({end}<{r}) : {(start<r)} {(end<r)} :{(start<r) ^ (end<r)}\n")
        if (start<r) ^ (end<r):
            cnt+=1
    print(cnt)