from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls_input = list(map(int, si.readline().split()))
# so.write(f"{}")

# a이상 b 미만의 소수
def Eratosthenes(a :int, b :int) -> list: 
    # True = 소수 , False = 소수아님 
    ls_input = [True]*b

    for i in range(2, int(b**0.5)+1):
        if ls_input[i]:
            for j in range(2*i, b, i):
                ls_input[j] = False

    ls_input[:2] = False, False
    ls_input[:a] = [False]*a
    return ls_input

# 입력
n = int(si.readline())
ls_input = []

for i in range(n):
    ls_input.append(int(si.readline()))
# print(ls_input)
#

# 에라토스테네스의 체
arr_Era_TF =Eratosthenes(0, max(ls_input))

ls_Eratos = [i for i in range(len(arr_Era_TF)) if arr_Era_TF[i]]
# print(ls_Eratos)

for i in ls_input:
    # print()
    for j in range(i//2, 1, -1):
        if j in ls_Eratos and i-j in ls_Eratos:
            so.write(f"{j} {i-j}\n")
            break