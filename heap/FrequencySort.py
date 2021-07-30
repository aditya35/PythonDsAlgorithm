class Number:
    def __init__(self,num,freq):
        self.num = num
        self.freq = freq

    def __lt__(self, other):
        return self.freq > other.freq

    def getNum(self):
        return self.num

    def getFreq(self):
        return self.freq

from collections import Counter
from heapq import heapify,heappop,heappush

def FrequencySort(arr):
    numFreq = Counter(arr)

    heap = []
    for key,val in numFreq.items():
        heappush(heap,Number(key,val))

    res = []
    while(len(heap)>0):
        num = heappop(heap)
        for i in range(num.getFreq()):
            res.append(num.getNum())
    return res

if __name__ == "__main__":
    print(FrequencySort([1,1,1,3,2,2,4]))