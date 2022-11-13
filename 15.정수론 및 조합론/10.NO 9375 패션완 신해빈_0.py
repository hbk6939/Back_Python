from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

T = int(si.readline())
dic = {}

def cnt_values(dic:dict)->list:
    cnts = []
    for v in dic:
        cnts.append(len(dic[v]))
        # print(f"cnt : {cnt}")
    return cnts

for i in range(T):
    n = int(si.readline())
    names = []; wears = []; dic = {}
    for j in range(n):
        name, wear = si.readline().strip().split()
        if wear in dic:
            dic[wear].append(name)
        else:
            dic[wear] = [name]

    # print(f"dic : {dic}")
    # print(f"len(dic) : {len(dic)}") # 의상 착용 가능 부위
    # print(f"cnt_values(dic) : {cnt_values(dic)}") # 부위별 의상 수
    cnt = 1
    for v in cnt_values(dic):
        cnt *= v+1
    so.write(f"{cnt-1}\n")