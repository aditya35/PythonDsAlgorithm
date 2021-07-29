def leftMax(arr:list):
    max1 = 0
    res = []
    for val in arr:
        max1 = max(max1,val)
        res.append(max1)
    return res

def rightMax(arr:list):
    max1 = 0
    res = []
    for i in range(len(arr)-1,-1,-1):
        max1 = max(max1,arr[i])
        res.append(max1)
    res.reverse()
    return res

def waterTrapped(lMax,rMax,arr):
    return [min(lMax[i],rMax[i]) - arr[i] for i in range(len(arr))]


if __name__ == "__main__":
    arr = [3,0,0,2,0,4]
    # arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    left = leftMax(arr)
    right = rightMax(arr)
    water = waterTrapped(left,right,arr)
    print(arr)
    print(left)
    print(right)
    print(water)
    print("Water Trapped is ",sum(water))