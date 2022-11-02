from sys import stdin as si, stdout as so

a, b, c = [int(si.readline()) for _ in range(3)]

res = str(a*b*c)
ls = [0]*10

# print(ls)

for s in res:
    ls[int(s)] += 1

for i in range(10):
    so.write(f"{ls[i]}\n")
