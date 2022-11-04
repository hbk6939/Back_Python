from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

N, M = map(int, si.readline().split())

dic_num_poket = {}
dic_poket_num = {}

for i in range(1, N+1):
    s = si.readline().strip()
    dic_num_poket[i] =  dic_num_poket.get(i, s) 
    dic_poket_num[s] =  dic_num_poket.get(s, i) 
    
arr = []
for i in range(M):
    s = si.readline().strip()
    if s.isdigit():
        arr.append(dic_num_poket[int(s)])
    else:
        arr.append(dic_poket_num[s])
    
# print()
print("\n".join(map(str, arr)))