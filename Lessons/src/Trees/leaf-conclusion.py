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

def get_leaves(root):
    leaves = []
    if root:
        if not root.left and not root.right:
            leaves.append(root.val)
        else:
            leaves.extend(get_leaves(root.left))
            leaves.extend(get_leaves(root.right))
    return sorted(leaves)

def main():
    nums = list(map(int, sys.stdin.readline().split()))
    root = None
    for num in nums:
        if num == 0:
            break
        root = insert(root, num)
    leaves = get_leaves(root)
    print(" ".join(map(str, leaves)))
    
if __name__ == "__main__":
    main()