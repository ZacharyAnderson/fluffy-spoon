from BST import BST_Node


def get_height(root):
    if not root:
        return 0
    return 1 + max(get_height(root.left_child),
                   get_height(root.right_child))


def check_balanced(bst):
    if not bst:
        return True
    return check_balanced(bst.right_child) and \
        check_balanced(bst.left_child) and \
        abs(get_height(bst.left_child) - get_height(bst.right_child)) <= 1

# Refactor into a better function


def is_balanced_helper(root):
    # a empty tree is balanced
    if not root:
        return 0

    left_height = is_balanced_helper(root.left_child)
    if left_height == -1:
        return -1

    right_height = is_balanced_helper(root.right_child)
    if right_height == -1:
        return -1

    if abs(right_height - left_height) > 1:
        return -1

    return max(left_height, right_height) + 1


def is_balanced(root):
    return is_balanced_helper(root) > -1


if __name__ == "__main__":
    test = BST_Node(10)
    test.insert(11)
    test.insert(9)
    test.insert(12)
    print(get_height(test))
    print(is_balanced(test))
