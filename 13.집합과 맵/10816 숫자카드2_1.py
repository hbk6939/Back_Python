from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

N = int(si.readline()) # 상근 카드수
# cards = list(map(int, si.readline().split()))
cards={}
for k in map(int, si.readline().split()):
    cards[k] = cards.get(k, 0) + 1
# print(cards)

M = int(si.readline()) # 몇 개 인지 확인할 숫자
check = list(map(int, si.readline().split()))

for v in check:
    so.write(f"{cards.get(v, 0)} ")