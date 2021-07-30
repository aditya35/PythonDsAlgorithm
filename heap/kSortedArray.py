from heapq import heapify, heappush, heappop
def sortKSorted(arr,k)->list:
    heap = []
    res  = []
    for val in arr :
        heappush(heap,val)
        if len(heap) > k:
            res.append(heappop(heap))

    while len(heap) > 0 :
        res.append(heappop(heap))

    return res

if __name__ == "__main__":
    print(sortKSorted([6,5,3,2,8,10,9],3))
