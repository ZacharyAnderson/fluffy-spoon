class MinStack:

    def __init__(self):
        self.stack = list()
        self.min = list()

    def __repr__(self):
        return repr(self.stack)

    def push(self, value):
        if not self.min or self.min[-1] > value:
            self.min.append(value)
        self.stack.append(value)

    def pop(self):
        popped_val = self.stack.pop()
        if popped_val == self.min[-1]:
            self.min.pop()

    def min_val(self):
        if self.min:
            return self.min[-1]
        return 0


if __name__ == "__main__":
    stack = MinStack()
    stack.push(3)
    stack.push(4)
    print(stack.min_val())
    stack.push(1)
    print(stack.min_val())
    stack.pop()
    print(stack.min_val())
