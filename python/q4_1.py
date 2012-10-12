#!/usr/bin/python

def main(root):
    """
    Check if tree is balanced
    """
    #return 0 <= max_depth(root) - min_depth(root) < 2
    return 0 <= depth(root, False) - depth(root, True) < 2

#def max_depth(node):
#    if node:
#        return max(max_depth(node.left_child), max_depth(node.right_child)) + 1
#    return 0
#
#def min_depth(node):
#    if node:
#        return min(min_depth(node.left_child), min_depth(node.right_child)) + 1
#    return 0

def depth(node, is_min):
    left = node.left_child
    right = node.right_child
    if node:
        return 1 + min(depth(left, is_min), depth(right, is_min)) if is_min else max(depth(left, is_min), depth(right, is_min))
    return 0


if __name__=='__main__':
    main()

