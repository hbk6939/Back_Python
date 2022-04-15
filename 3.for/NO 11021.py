# import time as t

from sys import stdin as si, stdout as so

n = int(si.readline())
# start = t.time()

res = ''

for i in range(1, n+1):
    a, b = map(int, si.readline().split())
    res += f'Case #{i}: {str(a+b)}\n'

so.write(f'{res}\n')

# so.write(f'{t.time() - start}초')