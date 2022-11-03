from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

def recursion(s, l, r, cnt):
    cnt+=1
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1, cnt)
    
def isPalindrome(s):
    cnt = 0
    return recursion(s, 0, len(s)-1, cnt)

for _ in range(int(si.readline())):
    s = si.readline().strip()
    a, b = isPalindrome(s)
    print(a, b)