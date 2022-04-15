from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())

def append_star(LEN):
    if LEN == 1:
        # print("append_star(1) 일 때 \n*")
        return '*'

    Stars = append_star(LEN//3)
    L = [] 
    
    for S in Stars:
        L.append(S*3)
    # print(f"append_star({LEN}) 일 때"+"1번\n"+'\n'.join(L))

    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    # print(f"append_star({LEN}) 일 때"+"2번\n"+'\n'.join(L))

    for S in Stars:
        L.append(S*3)
    # print(f"append_star({LEN}) 일 때"+"3번\n"+'\n'.join(L)+"\n------")
    return L

so.write("\n".join(append_star(n)))