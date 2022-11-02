from sys import stdin as si, stdout as so

up, down, V = map(int, si.readline().split())
# 낮에 +up 밤에 -down 높이 V

day = (V-down) // (up-down)

if (V-down) % (up-down):
    day += 1


so.write(f"{day}")
