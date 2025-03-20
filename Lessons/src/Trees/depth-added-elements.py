import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_and_get_depth(root, val, depth):
    if root is None:
        return Node(val), depth
    if val == root.val:
        return root, -1 
    elif val < root.val:
        root.left, inserted_depth = insert_and_get_depth(root.left, val, depth + 1)
        return root, inserted_depth
    else:
        root.right, inserted_depth = insert_and_get_depth(root.right, val, depth + 1)
        return root, inserted_depth

def main():
    nums = list(map(int, sys.stdin.readline().split()))
    root = None
    output_depths = []
    for num in nums:
        if num == 0:
            break
        root, depth = insert_and_get_depth(root, num, 1)
        if depth != -1:
            output_depths.append(str(depth))
    print(" ".join(output_depths))

if __name__ == "__main__":
    main()
    