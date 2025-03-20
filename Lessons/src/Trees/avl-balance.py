import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_height(root):
    if root is None:
        return -1
    return 1 + max(get_height(root.left), get_height(root.right))

def is_balanced(root):
    if root is None:
        return True
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    return (abs(left_height - right_height) <= 1) and is_balanced(root.left) and is_balanced(root.right)

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def main():
    input_vals = list(map(int, sys.stdin.readline().split()))
    root = None
    for val in input_vals:
        if val == 0:
            break
        root = insert(root, val)

    if is_balanced(root):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
