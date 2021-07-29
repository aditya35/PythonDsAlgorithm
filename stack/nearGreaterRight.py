def  nearestGreaterRight(arr):
    stack = list()
    output = list()

    for i in range(len(arr)-1,-1,-1):
        while len(stack) != 0 and stack[-1] < arr[i]:
            stack.pop()
        if len(stack) == 0:
            output.append(-1)
        else:
            output.append(stack[-1])

        stack.append(arr[i])

    return output


if __name__ == "__main__":
    # arr = [1,3,2,4]
    arr = [1,3,0,0,1,2,4]
    print(nearestGreaterRight(arr))