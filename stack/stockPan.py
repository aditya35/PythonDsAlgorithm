def stockPan(arr:list):
    stack = []
    res = []
    for i in range(len(arr)):
        while len(stack) > 0 and stack[-1][1] < arr[i]:
            stack.pop()
        if len(stack) == 0 :
            res.append(1)
        else:
            res.append(i-stack[-1][0])

        stack.append([i,arr[i]])
    return res

if __name__ == "__main__":
    arr = [100,80,60,70,60,75,85]
    print(stockPan(arr))