from BST import BST_Node


def list_of_depths(node, depth, levels=[]):
    if not node:
        return

    if depth == 0:
        levels.append(Node(node.value))
    else:
        if depth >= len(levels):
            levels.append(Node(node.value))
        else:
            level = levels[depth]
            while level:
                previous = level
                level = level.next
            previous.next = Node(node.value)
    list_of_depths(node.left_child, depth+1, levels)
    list_of_depths(node.right_child, depth+1, levels)

    return levels


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        nodes = list()
        nodes.append(str(self.value))
        curr = self.next
        while curr:
            nodes.append(str(curr.value))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'


if __name__ == "__main__":
    test = BST_Node(10)
    test.insert(11)
    test.insert(9)
    print(list_of_depths(test, 0))
