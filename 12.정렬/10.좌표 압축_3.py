from sys import stdin as si, stdout as so

n = int(si.readline())
row_arr = list(map(int, si.readline().split(" ")))

arr = sorted(set((row_arr)))

num_dict = {n : i for i, n in enumerate(arr)}

so.write(f"{' '.join([str(num_dict[num]) for num in row_arr])}\n")