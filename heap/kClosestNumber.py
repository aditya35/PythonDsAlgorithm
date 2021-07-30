from heapq import heapify,heappop,heappush
class number:
    def __init__(self,diff,val):
        self.diff = diff
        self.val = val

    def __lt__(self, other):
        return self.diff < other.diff

    def getDiff(self):
        return self.diff

    def getVal(self):
        return self.val

def kClosestNumber(arr,k,x):
    heap = []
    for val in arr:
        num = number(-1 * abs(val - x),val)
        heappush(heap,num)
        if len(heap) > k:
            heappop(heap)
    output = []
    while len(heap) > 0 :
        output.append(heappop(heap).getVal())
    return output

if __name__ == "__main__":
    print(kClosestNumber([5,6,7,8,9],k=3,x=7))