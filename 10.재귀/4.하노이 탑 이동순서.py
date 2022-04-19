import sys
from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

sys.setrecursionlimit(10**6)
ls = []

def hanoi(N :int, start :int, mid :int, end :int):
    if N == 1:
        # so.write(f"{start} {end}\n")
        ls.append(f"{start} {end}\n")
    else:
        # A -> C로 옮긴다고 가정할 떄
        # STEP 1 : N-1개를 A에서 B로 이동 (= start 지점의 N-1개의 원판을 mid 지점으로 옮긴다.)
        hanoi(N-1, start, end, mid)

        # STEP 2 : 1개를 A에서 C로 이동 (= start 지점의 N번째 원판을 to지점으로 옮긴다.)
        # so.write(f"{start} {end}\n")
        ls.append(f"{start} {end}\n")

        # STEP 3 : N-1개를 B에서 C로 이동 (= mid 지점의 N-1개의 원판을 to 지점으로 옮긴다.)
        hanoi(N-1, mid, start, end)
    

hanoi(int(si.readline()), 1, 2, 3)
so.write(f'{len(ls)}\n' + "".join(ls))