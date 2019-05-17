class MyQueue:

    def __init__(self):
        self.enqueue_stack = list()
        self.dequeue_stack = list()

    def __repr__(self):
        return repr((self.enqueue_stack, self.dequeue_stack))

    def enqueue(self, value):
        self.enqueue_stack.append(value)

    def dequeue(self):
        if not self.dequeue_stack and not self.enqueue_stack:
            raise Exception("Cannot dequeue an empty queue.")
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
            return self.dequeue_stack.pop()
        else:
            return self.dequeue_stack.pop()


if __name__ == "__main__":
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue)
    print(queue.dequeue())
    print(queue)
    queue.enqueue(16)
    print(queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue)
