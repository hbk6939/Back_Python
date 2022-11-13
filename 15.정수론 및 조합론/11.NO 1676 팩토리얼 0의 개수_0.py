from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수
n = int(si.readline())
res = 1
for i in range(1, n+1):
    # so.write(f"{res} * {i} =")
    res *= i
    # so.write(f"{res}\n")

cnt = 0
while True:
    if res%10:
        break
    else:
        res = res//10
        # so.write(f"res : {res}\n")
        cnt+=1

print(cnt)