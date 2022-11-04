from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

# 상근이 카드
N = int(si.readline()) # 숫자 카드의 개수
cards = list(map(int, si.readline().split())) # 카드에 적힌 숫자
# 
M = int(si.readline()) # 숫자 카드의 개수
check = list(map(int, si.readline().split())) # 카드에 적혀있는지 확인해야 하는 숫자

dic = {}

for k in cards:
    dic[k] = dic.get(k,0) + 1

for i in check:
    dic[i] = dic.get(i,0)

for i in check:
    so.write(f"{dic[i]} ")