from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())
row_arr = list(map(int, si.readline().split(" ")))

arr = sorted(set((row_arr)))
# print(arr)
num_dict = {n : i for i, n in enumerate(arr)}

# print(" ".join([str(num_dict[num]) for num in row_arr]))
so.write(f"{' '.join([str(num_dict[num]) for num in row_arr])}\n")
# [so.write(f"{num_dict[i]} ") for i in row_arr]