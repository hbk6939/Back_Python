from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

ls = []

for i in range(5):
    ls.append(int(si.readline()))
ls = sorted(ls)

print(int(sum(ls)/len(ls)))
print(ls[len(ls)//2])