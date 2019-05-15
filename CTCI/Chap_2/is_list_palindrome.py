from linkedList import Node, SinglyLinkedList


def is_list_palindrome(root):
    node_set = set()
    curr = root.root

    while curr:
        if curr.data in node_set:
            node_set.remove(curr.data)
        else:
            node_set.add(curr.data)
        curr = curr.next

    return len(node_set) <= 1


if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.insert(7)
    list1.insert(1)
    list1.insert(7)
    print(list1)
    print(is_list_palindrome(list1))
