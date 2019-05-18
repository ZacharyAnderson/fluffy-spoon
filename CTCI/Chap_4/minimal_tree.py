from BST import BST_Node


def minimal_tree(sorted_array):
    if not sorted_array:
        return None
    middle = len(sorted_array) // 2
    node = BST_Node(sorted_array[middle])
    node.left_child = minimal_tree(sorted_array[0:middle])
    node.right_child = minimal_tree(sorted_array[middle+1:])
    return node


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sorted_tree = minimal_tree(array)
    print(sorted_tree.print_tree_inorder(sorted_tree))
