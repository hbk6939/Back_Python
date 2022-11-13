from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수
n = int(si.readline())

cnt=0
while n>0:
      cnt += n//5
      n //= 5
print(cnt)