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

def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)

def main():
    nums = list(map(int, sys.stdin.readline().split()))
    root = None
    for num in nums:
        if num == 0:
            break
        root = insert(root, num)
    tree_height = height(root)
    print(tree_height)

if __name__ == "__main__":
    main()

