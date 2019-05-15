from linkedList import Node, SinglyLinkedList


def partition(root_node, partition):
    before = Node(0)
    before_head = before
    after = Node(0)
    after_head = after
    curr = root_node.root

    while curr:
        if curr.data < partition:
            before.next = curr
            before = before.next
        else:
            after.next = curr
            after = after.next

        curr = curr.next
    # last node in the list to be combined
    after.next = None
    # combines both lists
    before.next = after_head.next
    # sets the newly combined list to the old list
    root_node.root = before_head.next


if __name__ == "__main__":
    lst = SinglyLinkedList()
    lst.insert(1)
    lst.insert(4)
    lst.insert(3)
    lst.insert(2)
    print(lst)
    partition(lst, 3)
    print(lst)
