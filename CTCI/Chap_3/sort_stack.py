class SortStack:

    def __init__(self):
        self.stack = list()

    def __repr__(self):
        return repr(self.stack)

    def push(self, value):
        if self.is_empty():
            temp_stack = list()
            while self.stack:
                if value > self.peek():
                    temp_stack.append(self.stack.pop())
                else:
                    self.stack.append(value)
                    while temp_stack:
                        self.stack.append(temp_stack.pop())
            # Write other cases

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) != 0
