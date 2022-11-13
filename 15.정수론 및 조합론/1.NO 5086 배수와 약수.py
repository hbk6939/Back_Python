from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

while True:
    a, b = map(int, si.readline().split())
    if a==0 and b==0:
        break
    elif b%a==0: # a가 b의 약수면
        so.write('factor\n')
    elif a%b==0: # b가 a의 약수면(a가 b의 배수면)
        so.write('multiple\n')
    else:
        so.write('neither\n')