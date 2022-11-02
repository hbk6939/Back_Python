import sys; inp = sys.stdin.readline; out = sys.stdout.write;
# n = int(inp())
# ls = list(map(int, inp().split()))
# out(f"{}\n")

n = int(inp())
ls = [list(map(int, inp().split())) for _ in range(n)]

# print(ls)
# print(sorted(ls, key = lambda x: x[0]))
# print(sorted(ls, key = lambda x: x[1]))
# print(sorted(ls, key = lambda x: (x[0], x[1])))

ls.sort(key = lambda x: (x[0], x[1]))
[out(f"{ls[i][0]} {ls[i][1]}\n") for i in range(n)]