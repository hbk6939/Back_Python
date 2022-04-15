import sys; inp = sys.stdin.readline; out = sys.stdout.write;
# n = int(inp())
# ls = list(map(int, inp().split()))
# out(f"{}\n")

n = int(inp())
ls = [list(map(int, inp().split())) for _ in range(n)]

ls.sort()
[out(f"{ls[i][0]} {ls[i][1]}\n") for i in range(n)]