def nearestSmallerLeft(arr:list,outOfBoundIndex:int):
    stack = []
    res = []
    for i in range(len(arr)):
        while len(stack) > 0 and stack[-1][1] > arr[i] :
            stack.pop()
        if len(stack) == 0:
            res.append(outOfBoundIndex)
        else :
            res.append(stack[-1][0])
        stack.append([i,arr[i]])
    return res

def nearestSmallerRight(arr:list,outOfBoundIndex):
    stack = []
    res = []
    for i in range(len(arr)-1,-1,-1):
        while len(stack) > 0 and stack[-1][1] > arr[i]:
            stack.pop()
        if len(stack) == 0 :
            res.append(outOfBoundIndex)
        else :
            res.append(stack[-1][0])
        stack.append([i,arr[i]])
    res.reverse()
    return res

def maxAreaHistogram(nsl:list,nsr:list,arr:list):
    return [ ((nsr[i] - 1) - nsl[i]) * arr[i] for i in range(len(arr))]

if __name__ == "__main__":
    arr = [6,2,5,4,5,1,6]
    nsr = nearestSmallerRight(arr,len(arr))
    nsl = nearestSmallerLeft(arr,0)
    print("Max Area of Histogram is ",max(maxAreaHistogram(nsl,nsr,arr)))
