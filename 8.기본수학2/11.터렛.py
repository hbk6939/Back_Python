from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())

arr = [list(map(int, si.readline().split())) for _ in range(n)]

for i in range(n):
    x1 = arr[i][0]
    y1 = arr[i][1]
    r1 = arr[i][2]
    x2 = arr[i][3]
    y2 = arr[i][4]
    r2 = arr[i][5]

    origin_dist = ((x1-x2)**2 + (y1-y2)**2)**0.5

    # 1. 두 원의 중심이 같고, 반지름도 같을 때 ( 접점의 개수가 무한할 때 )
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    # 2. 접점이 없을 때
    # 2-1) 두 점 사이의 거리가 각 원의 반지름의 합보다 클 때
    elif origin_dist > r1+r2:
        print(0)
    # 2-2) 한 원 안에 다른 원이 있으면서 접점이 없을 때
    elif origin_dist < ((r1-r2)**2)**0.5:
        print(0)
    # 3. 접점이 한 개일 때
    # 3-1) 내접
    elif origin_dist == ((r1-r2)**2)**0.5:
        print(1)
    # 3-2) 외접
    elif origin_dist == r1 + r2:
        print(1)
    else:
        print(2)


