class Solution:
    def rangeSumBST(self, root, L, R):
        sum_val = 0
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if L <= root.val <= R:
                sum_val += root.val

            root = root.right

        return sum_val
        