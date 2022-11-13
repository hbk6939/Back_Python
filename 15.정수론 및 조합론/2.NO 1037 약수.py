from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

# A가 N의 약수인지? : A!=(1 or N)
# N의 진짜 약수 모두 있을 때 N은? 
N = int(si.readline()) # 약수의 개수
As = list(map(int, si.readline().split())) # 진짜 약수 A 배열


print(max(As)*min(As))