from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

n = int(si.readline())


def append_star(LEN):
    L = [] 
    print(f"--------------append_star({LEN})-------------------")

    if LEN == 1:
        print(f"L = {L}")
        print("append_star(1) 일 때 \n*\n----------------------")
        return '*'

    Stars = append_star(LEN//3)
    
    print(f"\nappend_star({LEN}) 일 때"+"1번째")
    for S in Stars:
        L.append(S*3)
        print(f"S = {S}")
        print(f"{S} X 3 = {S*3}")
        # print(L)
    print('\n'.join(L))

    print(f"\nappend_star({LEN}) 일 때"+"2번째")
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
        print(f"S = {S}")
        print(f"{S} + ' ' X {(LEN//3)} + {S} = {S+' '*(LEN//3)+S}")
        # print(L)
    print('\n'.join(L))

    print(f"\nappend_star({LEN}) 일 때"+"3번째")
    for S in Stars:
        L.append(S*3)
        print(f"S = {S}")
        print(f"{S} X 3 = {S*3}")
        # print(L)
    
    print('\n'.join(L)+"\n----------- 위의 도형을 return함 -----------\n")
    return L

so.write("\n".join(append_star(n)))