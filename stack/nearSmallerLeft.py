def nearSmallerLeft(arr: list):
    stack = []
    res = []
    for i in range(len(arr)):
        while len(stack) > 0 and stack[-1] > arr[i]:
            stack.pop()
        if len(stack) == 0:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(arr[i])
    return res


if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    print(nearSmallerLeft(arr))
