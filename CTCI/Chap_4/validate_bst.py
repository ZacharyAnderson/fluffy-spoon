from BST import BST_Node


def inorder_tree_traversal(root):
    tmp_list = list()
    if root:
        tmp_list = tmp_list + inorder_tree_traversal(root.left_child)
        tmp_list.append(root.value)
        tmp_list = tmp_list + inorder_tree_traversal(root.right_child)
    return tmp_list


def validate_bst(root):
    bst_list = inorder_tree_traversal(root)

    last_element = bst_list[0]
    for element in bst_list:
        if last_element > element:
            return False
        last_element = element
    return True

# slightly optimized solution would be to use a min/max approach


def check_bst(root, min=None, max=None):
    if not root:
        return True

    if (min and root.value <= min) or\
            (max and root.value > max):
        return False

    if not check_bst(root.left_child, min, root.value) or\
            not check_bst(root.right_child, root.value, max):
        return False

    return True


if __name__ == "__main__":
    test = BST_Node(10)
    test.insert(11)
    test.insert(8)
    test.insert(9)
    test.insert(12)
    print(check_bst(test))
