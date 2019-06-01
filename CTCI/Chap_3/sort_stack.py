class SortStack:

    def __init__(self):
        self.stack = list()

    def __repr__(self):
        return repr(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return -1

    def is_empty(self):
        return len(self.stack) == 0


def sort_stack(stack):
    tmp_stack = SortStack()
    while not stack.is_empty():
        curr = stack.pop()
        while not tmp_stack.is_empty() and tmp_stack.peek() > curr:
            stack.push(tmp_stack.pop())
        tmp_stack.push(curr)
    return tmp_stack


if __name__ == "__main__":
    stack = SortStack()
    stack.push(1)
    stack.push(3)
    stack.push(2)
    print(stack)
    stack.push(4)
    stack.push(5)
    print(stack)
    stack.push(6)
    stack.push(3)
    print(stack)
    print(sort_stack(stack))
