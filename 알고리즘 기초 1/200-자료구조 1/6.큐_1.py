import sys; inp = sys.stdin.readline; pri = sys.stdout.write

n = int(inp())
ls = []
res = []
start = 0

def is_emp(a, b):
    if b - a == 0:
        return 1
    else:
        return 0

for i in range(n):
    s = inp().rstrip()
    L = len(ls)

    if "push" in s:
        ls.append(int(s[5]))

    elif s == "pop":
        if is_emp(start, L):
            pri(f"{-1}\n")
        else:
            pri(f"{ls[start]}\n")
            start += 1

    elif s == "size":
        pri(f"{L - start}\n")

    elif s == "empty":
        pri(f"{is_emp(start, L)}\n")

    elif s == "front":
        pri(f"{-1}\n") if is_emp(start, L) else pri(f"{ls[start]}\n")

    elif s == "back":
        pri(f"{-1}\n") if is_emp(start, L) else pri(f"{ls[-1]}\n")

