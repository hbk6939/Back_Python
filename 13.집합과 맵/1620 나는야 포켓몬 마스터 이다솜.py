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
    
res = ""
for i in range(M):
    s = si.readline().strip()
    try:
        n = int(s)
        res += f"{dic_num_poket[n]}\n"
    except:
        res += f"{dic_poket_num[s]}\n"
# print()
print(res)
