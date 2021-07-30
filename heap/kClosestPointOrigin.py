import math
from heapq import heappop,heappush
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dist0 = math.sqrt(math.pow(x,2)+math.pow(y,2))

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __lt__(self, other):
        return self.dist0 > other.dist0

def kClosestPointOrigin(arr,k):
    heap = []
    for [x,y] in arr:
        heappush(heap,Point(x,y))
        if len(heap) > k:
            heappop(heap)
    res = []
    while len(heap)>0:
        point = heappop(heap)
        res.append([point.getX(),point.getY()])
    res.reverse()
    return res

if __name__ == "__main__":
    print(kClosestPointOrigin([[1,2],[-2,2],[5,8],[0,1]],3))