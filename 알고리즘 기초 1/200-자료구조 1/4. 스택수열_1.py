import sys; inp = sys.stdin.readline; outp = sys.stdout.write
# n = int(inp())
# ls = list(map(int, inp().split()))
# ls = [int(inp()) for _ in range(n)]
# outp(f"{}\n")

def my_stack():
    n = int(inp())
    stack, res, cnt = [], [], 1

    for _ in range(n):
        num = int(inp())
        while num >= cnt:
            stack.append(cnt)
            res.append('+')
            cnt += 1
        if stack[-1] != num:
            return 'NO'
        else:
            stack.pop()
            res.append('-')
        # print(f"num = {num}, cnt = {cnt}\nstack = {stack}\nres = {res}\n")
    return '\n'.join(res)

outp(my_stack())