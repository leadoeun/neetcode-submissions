class MinStack:

    def __init__(self):
        self.slist = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.slist.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.minStack[-1] == self.slist[-1]:
            self.minStack.pop()
        return self.slist.pop()

    def top(self) -> int:
        return self.slist[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
