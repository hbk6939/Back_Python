from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())

def VPS(s :str)->bool:
    ls = []
    for i in s:
        if i == "(":
            ls.append(i)
        else:
            if len(ls) == 0:
                return 'NO'
            else:
                ls.pop()
    if len(ls) > 0:
        return 'NO'
    else:
        return 'YES'

for i in range(n):
    word = si.readline().strip()
    print(VPS(word))