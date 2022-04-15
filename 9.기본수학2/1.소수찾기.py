from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())
ls = list(map(int, si.readline().split()))

def is_prime(n :int) -> bool:
    if n == 1:
        return False
    
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(n**0.5)+1):
        # x가 해당 수로 나누어떨어진다면
        if n%i == 0:
            return False # 소수 아님
    return True # 소수임
        
cnt = 0

for i in range(n):
    if is_prime(ls[i]):
        cnt += 1

print(cnt)






