from sys import stdin as si, stdout as so

n_max = float("-inf")
inx = 0

for i in range(1,10):
    num = int(si.readline())
    if num > n_max:
        n_max = num
        # print("\n",n_max)
        inx = i

print(f"{n_max}\n{inx}")
so.write(f"{n_max}\n{inx}")