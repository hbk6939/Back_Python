from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())

def star(a :int)->int:
    if a == 1:
        return '*'
    new_star = star(a//3)
    res = []

    for i in new_star:
        res.append(i*3)
    for i in new_star:
        res.append(i + " "*(a//3) + i)
    for i in new_star:
        res.append(i*3)
    return res

print("\n".join(star(n)))
    
        


