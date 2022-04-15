from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

# a이상 b 미만의 소수
def Eratosthenes(start :int, end :int) -> list: 
    # True = 소수 , False = 소수아님 
    ls = [True]*end

    for i in range(2, int(end**0.5)+1):
        if ls[i]:
            for j in range(2*i, end, i):
                ls[j] = False

            # j = 2
            # while i*j < end:
            #     ls[i*j] = False
            #     j += 1
                
    ls[:2] = False, False
    ls[:start] = [False]*start
    return ls

# a이상 b미만 배열의 참값 개수
def num_of_True(start :int, end :int, arr :bool) -> int:
    cnt = 0
    for i in range(start, end):
        if arr[i]:
            cnt += 1
    return cnt

arr_input = []

while True:
    n = int(si.readline())
    if n == 0:
        break
    arr_input.append(n)

# bool
ls = Eratosthenes(min(arr_input), 2*max(arr_input)+1) 


for i in range(len(arr_input)):
    res = num_of_True(arr_input[i]+1, 2*arr_input[i]+1, ls)
    so.write(f"{res}\n")
        
