from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

# 방향이 1번 나온곳(idx)이 행열 max값
# 2번 후의 방향이 같으면 1번후의 값이 변의 길이
# 필요변수 : 방향배열, 길이배열, 뱡향횟수배열, 큰사각형, 작은사각형

N = int(si.readline())
B=1; S=1; 
ls_cnt=[0]*5; ls_di=[]; ls_len=[]

for i in range(6):
    a, b = map(int, si.readline().split())
    ls_di.append(a); ls_len.append(b)
    ls_cnt[a]+=1

for i in range(6):
    if ls_cnt[ls_di[i]] == 1: # 방향이 1번만 나왔으면
        B*=ls_len[i] # 큰사각형
        
    n=(i+1)%6 # 다음 idx
    nn=(i+2)%6 # 다다음 idx
    if ls_di[i] == ls_di[nn]: # 현재와 2번째 후 idx가 같으면
        S*=ls_len[n]

print((B-S)*N)