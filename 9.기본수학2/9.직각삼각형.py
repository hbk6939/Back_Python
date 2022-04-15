from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

while True:
    x, y, z = map(int, si.readline().split())
    if x==0 and y==0 and z==0:
        break
    
    if (x**2 + y**2) == z**2:
       print("right")
    elif (x**2 + z**2) == y**2:
       print("right")
    elif (y**2 + z**2) == x**2:
       print("right")
    else:
       print("wrong")
