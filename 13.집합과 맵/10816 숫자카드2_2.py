from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")
from collections import Counter

N = int(si.readline()) # 상근 카드수
cards = Counter(si.readline().split())

M = int(si.readline()) # 몇 개 인지 확인할 숫자
check = si.readline().split()

print(' '.join(f'{cards.get(k,0)}' for k in check))