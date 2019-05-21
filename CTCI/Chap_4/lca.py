from BST import BST_Node


def lowest_common_ancestor(root, node1, node2):

    if root is None:
        return None

    # if either nodes presence is found we return the root node
    if root.value == node1 or root.value == node2:
        return root.value

    left_lca = lowest_common_ancestor(root.left_child, node1, node2)
    right_lca = lowest_common_ancestor(root.right_child, node1, node2)

    if left_lca and right_lca:
        return root.value

    return left_lca if left_lca is not None else right_lca


if __name__ == "__main__":
    test = BST_Node(10)
    test.insert(12)
    test.insert(8)
    test.insert(9)
    test.insert(11)
    test.insert(13)
    print(lowest_common_ancestor(test, 11, 12))
