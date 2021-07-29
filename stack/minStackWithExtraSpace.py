class minStackExtraSpace:
    def __init__(self):
        self.stack = []
        self.ss = []

    def push(self,val):
        self.stack.append(val)
        if len(self.ss) == 0 or val < self.ss[-1]:
            self.ss.append(val)

    def pop(self):
        popped = self.stack.pop()
        if popped == self.ss[-1]:
            self.ss.pop()
        return popped

    def minElement(self):
        if len(self.ss) > 0 :
            return self.ss[-1]
        else:
            return -1

if __name__ == "__main__":
    ms = minStackExtraSpace()
    ms.push(18)
    ms.push(19)
    ms.push(29)
    ms.push(15)
    print(ms.minElement())
    print(ms.pop())