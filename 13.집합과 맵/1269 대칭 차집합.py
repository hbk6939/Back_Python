from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

s = si.readline().strip()
s_set = set()
cnt = len(s)

for i in range(cnt):
    for j in range(i+1, cnt+1):
        s_set.add(s[i:j])

# print(s_set)
print(len(s_set))

# 0번  갯수 : 1 2 3 4 5 
# 1번  갯수 : 2 3 4 5
# 2번  갯수 : 3 4 5
# 3번  갯수 : 4 5
# 4번  갯수 : 5