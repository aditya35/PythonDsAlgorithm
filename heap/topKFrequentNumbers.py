class numbers:
    def __init__(self,num,freq):
        self.num = num
        self.freq = freq

    def getNum(self):
        return self.num

    def getFreq(self):
        return self.freq

    def setFreq(self,freq):
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq

from collections import Counter
from heapq import heapify,heappop,heappush

def topKFrequentNumbers(arr,k):
    freqMap = Counter(arr)
    print(freqMap)
    heap  = []
    for key,val in freqMap.items():
        numFreq = numbers(key,val)
        heappush(heap,numFreq)
        if len(heap) > k:
            heappop(heap)
    return [ num.getNum() for num in heap]

if __name__ == "__main__":
    print(topKFrequentNumbers([1,1,1,3,2,2,4],2))