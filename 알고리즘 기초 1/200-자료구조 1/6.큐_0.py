import sys; inp = sys.stdin.readline; pri = sys.stdout.write
# n = int(inp())
# ls = list(map(int, inp().split()))
# ls = [int(inp()) for _ in range(n)]
# pri(f"{}\n")

n = int(inp())
ls = [0] * n
start = 0
end = 0


for i in range(n):
    s = inp().split()
    if s[0] == "push":
        ls[end] = int(s[1])
        end += 1
    elif s[0] == "pop":
        if end - start == 0:
            pri(f"{-1}\n")
        else:
            pri(f"{ls[start]}\n")
            start += 1
    elif s[0] == "size":
        pri(f"{end-start}\n")

    elif s[0] == "empty":
        if end - start:
            pri(f"{0}\n")
        else:
            pri(f"{1}\n")
    elif s[0] == "front":
        if end - start:
            pri(f"{ls[start]}\n")
        else:
            pri(f"{-1}\n")
    elif s[0] == "back":
        if end - start:
            pri(f"{ls[end-1]}\n")
        else:
            pri(f"{-1}\n")

    # pri(f"{ls[start:end]} start:{start} end:{end}\n\n")
