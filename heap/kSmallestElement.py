from heapq import heapify,heappop,heappush,heappushpop
def kSmallestElement(arr,k):
    heap  = []
    heapify(heap)

    for val in arr :
        heappush(heap,-1 *val)
        if len(heap) > k :
            heappop(heap)

    return heappop(heap) * -1

if __name__ == "__main__":
    print(kSmallestElement([7,10,4,3,20,15],1))