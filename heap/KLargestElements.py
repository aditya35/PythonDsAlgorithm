from heapq import heapify, heappop,heappush,heappushpop
def kLargestElements(arr,k):
    heap = []

    for val in arr:
        heappush(heap,val)
        if len(heap) > k :
            heappop(heap)
    return heap

if __name__ =="__main__":
    print(kLargestElements([7,10,4,3,20,15],3))