import sys

inp = sys.stdin.readline
outp = sys.stdout.write

ls = sys.stdin.read().rstrip().split("\n")

L_stack = list(ls[0])
R_stack = []

for i in ls[2:]:
    if i[0] == "L" and L_stack: # 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
        R_stack.append(L_stack.pop())
    
    elif i[0] == "D" and R_stack: # 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
        L_stack.append(R_stack.pop())

    elif i[0] == "B" and L_stack: # 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
        L_stack.pop()

    elif i[0] == "P": # 문자를 커서 왼쪽에 추가함
        L_stack.append(i[2])
        
R_stack.reverse()
outp(''.join(L_stack + R_stack))