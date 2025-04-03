import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def get_one_child_nodes(root):
    one_child_nodes = []
    if root:
        if (root.left and not root.right) or (not root.left and root.right):
            one_child_nodes.append(root.val)
        one_child_nodes.extend(get_one_child_nodes(root.left))
        one_child_nodes.extend(get_one_child_nodes(root.right))
    return sorted(one_child_nodes)

def main():
    nums = list(map(int, sys.stdin.readline().split()))
    root = None
    for num in nums:
        if num == 0:
            break
        root = insert(root, num)

    one_child_nodes = get_one_child_nodes(root)
    print(" ".join(map(str, one_child_nodes)))

if __name__ == "__main__":
    main()
    
    