from sys import stdin as si, stdout as so

x = int(si.readline())

# n번줄 분모분자의 합 = n+1
# 짝수번째 줄은 오름차순 (1/n, 2/n-1, ......, n-1/2, n/1)
# 홀수번째 줄은 내림차순 (n/1, n-1/2, ......, 2/n-1, 1/n)

# 줄마다 a_n = 1 + d
# 등차수열의 합 = n(a+l)/2 = n{2a+(n-1)d}/2

def count_line(x :int) -> int: # 줄수 판별
    a = 0 # 초기값
    line = 0 # 줄수
    while a < x: # 초기값이 입력값 이상 break
        a += line+1
        line += 1
    return a, line

line = count_line(x)[1] # 줄 수
a = count_line(x)[0] -line # 이전까지 값
cnt = x-a

# print(f"{a} 줄:{line} 줄의 몇번째인지:{cnt}")

# 짝수번째 줄은 오름차순 (1/n, 2/n-1, ......, n-1/2, n/1) cnt/line+1-cnt
# 홀수번째 줄은 내림차순 (n/1, n-1/2, ......, 2/n-1, 1/n) line+1-cnt/cnt

if line % 2 == 0: # 줄이 짝수일 경우
    # print()
    print(f"{cnt}/{line+1-cnt}")
else:
    # print()
    print(f"{line+1-cnt}/{cnt}")













