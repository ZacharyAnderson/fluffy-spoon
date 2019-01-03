class MaxStack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.stack = Stack()
        self.maxes_stack = Stack()

    def push(self, item):
        """Push new item to stack"""
        self.stack.push(item)
        
        if self.maxes_stack.peek() is None or item >= self.maxes_stack.peek():
            self.maxes_stack.push(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        item = self.stack.pop()
        
        if item == self.maxes_stack.peek():
            self.maxes_stack.pop()

        return self.items.pop()

    def get_max(self):
        return self.maxes_stack.peek()
