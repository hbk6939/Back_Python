from sys import stdin as si, stdout as so
# n = int(si.readline())
# ls = list(map(int, si.readline().split()))
# so.write(f"{}")

def merge_sort(arr):
    cnt, res = 0, 0    
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid) # 전반부 정렬
        sort(mid, high) # 후반부 정렬
        merge(low, mid, high) # 병합

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid: # 왼쪽 배열 부분이 남은경우
            temp.append(arr[l])
            l += 1
        while h < high: # 오른쪽 배열 부분이 남은 경우
            temp.append(arr[h])
            h += 1

        for i in range(low, high): # 결과를 arr에 저장
            arr[i] = temp[i - low]
            

    return sort(0, len(arr))

arr_size, store_num = map(int, si.readline().split())
ls = list(map(int, si.readline().split()))

merge_sort(ls)
print(ls)


# print(arr_size, store_num)
# print(arr)