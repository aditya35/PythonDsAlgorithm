import math


def nearSmallLeft(arr,outOfBoundIndex):
    stack = []
    res = []
    for i in range(len(arr)):
        while len(stack) > 0 and stack[-1][1] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            res.append(outOfBoundIndex)
        else:
            res.append(stack[-1][0])
        stack.append([i,arr[i]])
    return res

def nearSmallRight(arr,outOfBoundIndex):
    stack = []
    res = []

    for i in range(len(arr)-1,-1,-1):
        while len(stack) > 0 and stack[-1][1] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            res.append(outOfBoundIndex)
        else :
            res.append(stack[-1][0])
        stack.append([i,arr[i]])
    res.reverse()
    return res

def maximumAreaHistogram(arr,nsr,nsl):
    return [(((nsr[i] - 1) - nsl[i]) * arr[i]) for i in range(len(arr))]

if __name__ == "__main__":
    bin_matrix = [[0,1,1,0] , [1,1,1,1] , [1,1,1,1] , [1,1,0,0]]
    histogram = [0] * len(bin_matrix[0])
    maxArea = -math.inf
    for i in range(len(bin_matrix)):
        for j in range(len(bin_matrix[i])):
            if bin_matrix[i][j] == 0:
                histogram[j] = 0
            else :
                histogram[j] += bin_matrix[i][j]
        area = maximumAreaHistogram(histogram,nearSmallRight(histogram,len(histogram)+1),nearSmallLeft(histogram,0))
        maxArea = max(maxArea,max(area))