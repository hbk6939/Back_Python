from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# ls = [int(si.readline()) for _ in range(n)]
# so.write(f"{}\n")

stack = []
plus_minus = []
flag_max = 0

n = int(si.readline())

for i in range(n):
    num = int(si.readline())
    if num > flag_max:
        for j in range(num):
            stack.append(j+1)
            plus_minus.append('+')
        flag_max = num
    
    if stack[-1] == num:
        stack.pop()
        plus_minus.append('-')
    else:
        print('NO')

print(stack)
print(plus_minus)





