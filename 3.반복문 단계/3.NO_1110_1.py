from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(input()) # 0~99
compare = n
new_sum = 0

# 수가 10보다 작다면 앞에 0을 붙여 두 자리 수
# 각 자리의 숫자를 더한다
cnt = 0
while(True):
    if n < 10:n*10
    left_num = n//10
    right_num = n%10
    new_sum = left_num + right_num

    n = right_num*10 + new_sum%10
    cnt += 1
    # print(f"{left_num} + {right_num} = {new_sum}, next = {n}, cnt = {cnt}")
    if n == compare:
        break
# 주어진 수(n)의 가장 오른쪽 자리 수와 
# 앞에서 구한 합(new_n)의 가장 오른쪽 자리 수를 이어 붙이기

print(cnt)