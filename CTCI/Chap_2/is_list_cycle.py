from linkedList import Node, SinglyLinkedList


def is_list_a_cycle(root):
    curr = root.root
    runner = curr

    while curr:
        curr = curr.next
        runner = runner.next.next
        if curr == runner:
            break

    if runner is None or runner.next is None:
        return None

    curr = root.root
    while curr != runner:
        curr = curr.next
        runner = runner.next

    return runner


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = head
    print(head)
