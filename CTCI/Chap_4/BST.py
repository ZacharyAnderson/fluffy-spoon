class BST_Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return repr(self.value)

    def insert(self, value):
        if self.value:
            if value > self.value:
                if self.right_child is None:
                    self.right_child = BST_Node(value)
                else:
                    self.right_child.insert(value)
            elif value < self.value:
                if self.left_child is None:
                    self.left_child = BST_Node(value)
                else:
                    self.left_child.insert(value)
        else:
            self.value = value

    def print_tree_inorder(self, root):
        tmp_list = list()
        if root:
            tmp_list = self.print_tree_inorder(root.left_child)
            tmp_list.append(root.value)
            tmp_list = tmp_list + self.print_tree_inorder(root.right_child)
        return tmp_list

    def print_tree_preorder(self, root):
        tmp_list = list()
        if root:
            tmp_list.append(root.value)
            tmp_list = tmp_list + self.print_tree_preorder(root.left_child)
            tmp_list = tmp_list + self.print_tree_preorder(root.right_child)
        return tmp_list

    def print_tree_postorder(self, root):
        tmp_list = list()
        if root:
            tmp_list = tmp_list + self.print_tree_postorder(root.left_child)
            tmp_list = tmp_list + self.print_tree_postorder(root.right_child)
            tmp_list.append(root.value)
        return tmp_list


if __name__ == "__main__":
    test = BST_Node(10)
    test.insert(11)
    test.insert(9)
    print(test.print_tree_inorder(test))
    print(test.print_tree_preorder(test))
    print(test.print_tree_postorder(test))
