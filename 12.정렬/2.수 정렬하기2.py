import sys
I = sys.stdin.readline
O = sys.stdout.write
# n = int(I())
# ls = list(map(int, I.split()))
# O(f"{}\n")

n = int(I())
ls = [int(I()) for i in range(n)]

# [O(f"{i}\n") for i in sorted(ls)]

ls.sort()
[O(f"{i}\n") for i in ls]