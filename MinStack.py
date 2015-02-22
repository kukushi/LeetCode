class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    # @param x, an integer
    # @return an integer

    def push(self, x):
        self.stack.append(x)

        if len(self.minStack) == 0:
            self.minStack.append(x)
        elif x <= self.minStack[-1]:
                self.minStack.append(x)


    # @return nothing
    def pop(self):
        toPop = self.stack.pop()
        if self.minStack[-1] == toPop:
            self.minStack.pop()

    # @return an integer
    def top(self):
        return self.stack[len(self.stack) - 1]

    # @return an integer
    def getMin(self):
        return self.minStack[len(self.minStack) - 1]