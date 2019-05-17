class SetOfStacks:

    def __init__(self):
        self.set_of_stacks = list()
        self.max_height = 5

    def __repr__(self):
        return repr(self.set_of_stacks)

    def push(self, data):
        if not self.set_of_stacks:
            stack_list = list()
            stack_list.append(data)
            self.set_of_stacks.append(stack_list)
        last_stack = self.set_of_stacks[-1]
        if last_stack and len(last_stack) <= 5:
            last_stack.append(data)
        else:
            new_stack = list()
            new_stack.append(data)
            self.set_of_stacks.append(new_stack)


if __name__ == "__main__":
    pancakes = SetOfStacks()
    pancakes.push(1)
    pancakes.push(2)
    pancakes.push(3)
    pancakes.push(4)
    pancakes.push(5)
    pancakes.push(6)
    pancakes.push(6)
    pancakes.push(6)
    pancakes.push(6)
    print(pancakes)
