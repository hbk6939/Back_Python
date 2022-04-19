from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}\n")

n = int(si.readline())
stack = [0]*n
length = 0

for i in range(n):
    word = si.readline().split()

    if word[0] == "push":
        length += 1
        stack[length-1] = int(word[1])

    if word[0] == "pop":
        if length == 0:
            so.write(f"{-1}\n")
        else:
            length -= 1
            so.write(f"{stack[length]}\n")
            stack[length] = 0

    if word[0] == "size":
        so.write(f"{length}\n")

    if word[0] == "empty":
        if length == 0:
            so.write(f"{1}\n")
        else:
            so.write(f"{0}\n")

    if word[0] == "top":
        if length == 0:
            so.write(f"{-1}\n")
        else:
            so.write(f"{stack[length-1]}\n")