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

def get_two_children_nodes(root):
    two_children_nodes = []
    if root:
        if root.left and root.right:
            two_children_nodes.append(root.val)
        two_children_nodes.extend(get_two_children_nodes(root.left))
        two_children_nodes.extend(get_two_children_nodes(root.right))
    return sorted(two_children_nodes)

def main():
    nums = list(map(int, sys.stdin.readline().split()))
    root = None
    for num in nums:
        if num == 0:
            break
        root = insert(root, num)
    two_children_nodes = get_two_children_nodes(root)
    print(" ".join(map(str, two_children_nodes)))
    
if __name__ == "__main__":
    main()
    