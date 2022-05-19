import sys; inp = sys.stdin.readline; pri = sys.stdout.write
# n = int(inp())
# ls = list(map(int, inp().split()))
# ls = [int(inp()) for _ in range(n)]
# pri(f"{}\n")

ls = [int(inp()) for _ in range(int(inp()))]

# stack 숫자, res +-기호, before_max숫자
stack:int = []
sb:str = []
before_max:int = 0
result:int = [] 

for i in ls:
    # pri(f"\n{i}\n")
    if i > before_max:
        for j in range(before_max+1, i+1):
            stack.append(j)
            sb.append('+')
            # pri(f'push{j}, stack= {stack}, result = {result}, operater = +\n')
        before_max = i
        # pri(f'스텍 최근값 {stack[-1]} == 입력값 {i}\n')
    elif stack[-1] != i:
        # pri(f'스텍 최근값 {stack[-1]} != 입력값 {i} \n')
        pri('NO\n')
        quit()
    stack.pop()
    sb.append('-')
    # result.append(i)
    # pri(f'stack.pop() -> {j}삭제 \nstack= {stack}, result = {result}, operater = -\n')

pri('\n'.join(sb))
