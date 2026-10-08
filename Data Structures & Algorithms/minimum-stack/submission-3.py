class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.min = 2**31
        # self.minTwo = 99999

    def push(self, val: int) -> None:
        self.minStack.append(self.min)
        if val < self.min: # keep track of min
            
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        # if popped == self.min:
        self.min = self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
