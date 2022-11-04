import heapq
def heap_sort(arr:list)->list:
    heap = []
    res = []
    for v in arr:
        heapq.heappush(heap, v)
    for i in range(len(heap)):
        res.append(heapq.heappop(heap))
    return res


arr = [1, 5, 2, 6, 3, 7, 4]
ls = arr[1:5]
ls = heap_sort(ls)

print(ls)