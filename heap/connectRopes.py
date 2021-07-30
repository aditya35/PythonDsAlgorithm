from heapq import heappop, heappush,heapify
def connectRopes(arr):
    heap = arr
    heapify(heap)
    cost = 0

    # until pair exists
    while len(heap)>1:
        r1 = heappop(heap)
        r2 = heappop(heap)
        rn = r1 + r2
        cost += rn
        heappush(heap,rn)

    return cost


if __name__ == "__main__":
    print(connectRopes([1,2,3,4,5]))