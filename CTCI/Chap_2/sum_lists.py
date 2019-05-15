from linkedList import Node, SinglyLinkedList


def sum_lists(list1, list2):
    list1_int = list_to_int(list1)
    list2_int = list_to_int(list2)
    sum_of_lists = int(list1_int) + int(list2_int)
    sum_of_lists_string = str(sum_of_lists)

    new_list = Node()
    head = new_list

    for ch in sum_of_lists_string[::-1]:
        new_node = Node(data=ch)
        new_list.next = new_node
        new_list = new_list.next

    final_list = SinglyLinkedList()
    final_list.root = head.next

    return final_list


def list_to_int(input_list):
    list_stack = list()
    curr = input_list.root
    while curr:
        list_stack.append(curr.data)
        curr = curr.next

    tmp_int = ""
    while list_stack:
        tmp_int += str(list_stack.pop())
    return tmp_int


if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.insert(7)
    list1.insert(1)
    list1.insert(6)
    print(list1)
    list2 = SinglyLinkedList()
    list2.insert(5)
    list2.insert(9)
    list2.insert(2)
    print(list2)
    new_list = sum_lists(list1, list2)
    print(new_list)
