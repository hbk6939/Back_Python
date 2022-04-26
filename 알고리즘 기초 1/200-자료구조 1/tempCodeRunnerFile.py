import sys

inp = sys.stdin.readline
outp = sys.stdout.write
# n = int(inp())
# ls = list(map(int, inp().split()))
# ls = [int(inp()) for _ in range(n)]
# outp(f"{}\n")

s = list(inp().strip())
n = int(inp())

point = len(s)

for i in range(n):
    cmd = inp().strip().split()
    if cmd[0] == "L":
        if point > 0:
            point -= 1
    if cmd[0] == "D":
        if point < len(s):
            point += 1
    if cmd[0] == "B":
        if point > 0:
            point -= 1
    if cmd[0] == "P":
        s.insert(point, cmd[1])
        point += 1
    # outp("".join(s)+'\n')
    
outp("".join(s)+'\n')