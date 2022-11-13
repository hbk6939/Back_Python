from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

# nCm 의 끝자리 $0$의 개수를 출력하는 프로그램을 작성하시오.
n, m = map(int, si.readline().split())
son = 1; mom = 1
for i in range(m):
    son *= n-i
    mom *= m-i
res = son//mom
# print(res)


def FunctionName(args):
    return 0
cnt=0
while n>0:
      cnt += n//5
      n //= 5