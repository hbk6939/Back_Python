from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())
ls = [0]*8001 # 인덱스번호-4000 = 입력된 숫자 갯수

for i in range(n): # 입력된 숫자를 ls 배열에
    ls[int(si.readline())+4000] += 1

arr = [] # arr : 입력된 숫자 배열
for i in range(len(ls)):
    for j in range(ls[i]):
        arr.append(i-4000)
# print(arr)

def mod()->int:
    m = max(ls)
    cnt = mod_num = 0
    for i in range(len(ls)):
        if ls[i] == m:
            cnt += 1
            mod_num = i-4000
        if cnt == 2:
            mod_num = i-4000 # 인덱스 번호-4000 == 입력된 숫자
            break
    return mod_num

# print()
so.write(f"{int(round(sum(arr)/n, 0))}\n") # 산술평균
so.write(f"{arr[n//2]}\n") # 중앙값
so.write(f"{mod()}\n") # 최빈값 : 여러 개 있을 때에는 최빈값 중 두 번째로 "작은" 값을 출력
so.write(f"{arr[n-1]-arr[0]}\n") # 범위