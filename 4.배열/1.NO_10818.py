# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
from sys import stdin as si, stdout as so

N = int(input())
arr = list(map(int, si.readline().split()))

max = float('-inf')
min = float('inf')

for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i

so.write(f'{min} {max}')
            



