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

def find_second_largest(root):
    if root is None or (root.left is None and root.right is None):
        return None  
    current = root
    parent = None
    while current.right:
        parent = current
        current = current.right
    if current.left:
        temp = current.left
        while temp.right:
            temp = temp.right
        return temp.val
    else:
        return parent.val

def main():
    nums = list(map(int, sys.stdin.readline().split()))
    root = None
    for num in nums:
        if num == 0:
            break
        root = insert(root, num)
    second_largest = find_second_largest(root)
    print(second_largest)

if __name__ == "__main__":
    main()
