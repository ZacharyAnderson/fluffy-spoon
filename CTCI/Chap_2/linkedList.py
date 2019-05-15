class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.root = None

    def __repr__(self):
        nodes = list()
        curr = self.root
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def insert(self, data):
        if not self.root:
            self.root = Node(data=data)
            return
        curr = self.root
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)

    def find(self, key):
        curr = self.root
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def delete_node(self, key):
        curr = self.root
        prev = None
        while curr:
            if curr.data == key:
                if prev is None:
                    self.root = curr.next
                else:
                    prev.next = curr.next
                    curr.next = None
            prev = curr
            curr = curr.next

    def reverse_list(self):
        curr = self.root
        prev = None
        future = None

        while curr:
            future = curr.next
            curr.next = prev
            prev = curr
            curr = future
        self.root = prev

    def remove_dups(self):
        data_set = set()
        curr = self.root
        previous = None
        while curr:
            if curr.data in data_set:
                previous.next = curr.next
            else:
                data_set.add(curr.data)
                previous = curr
            curr = curr.next

    def length(self):
        """
            Helper function that returns length of list
        """
        curr = self.root
        length_count = 0
        while curr:
            length_count += 1
            curr = curr.next
        return length_count

    def return_kth_to_last_node(self, k):
        """
            Returns the Kth to last node, where K
            is an integer received as input
        """
        length = self.length()
        node_to_return = length - k
        if k > length or k < 1:
            raise ValueError("Invalid input")
        curr = self.root
        for _ in range(node_to_return):
            curr = curr.next
        return curr

    def delete_middle_node(self, node_to_delete):
        """
            deletes a node not necessarily in the middle,
            but the node cannot be the first or last node.
            Function will delete first occurence of node.
            Input - node to be deleted
            Output - None
        """
        curr = self.root
        prev = None
        while curr:
            if curr.data == node_to_delete and prev is not None and curr.next:
                prev.next = curr.next
                curr = curr.next
            prev = curr
            curr = curr.next


if __name__ == "__main__":
    lst = SinglyLinkedList()
    print(lst)
    lst.insert("text")
    lst.insert("test")
    lst.insert("test")
    lst.insert("yup")
    print(lst)
    lst.delete_middle_node("yup")
    print(lst)
