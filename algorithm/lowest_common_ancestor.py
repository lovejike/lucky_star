class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def lowest_common_ancestor(self, root, a, b):
        if root is None or root == a or root == b:
            return root
        left = self.lowest_common_ancestor(root.left, a, b)
        right = self.lowest_common_ancestor(root.right, a, b)
        if left is not None and right is not None:
            return root
        if left is None and right is not None:
            return right
        if right is None and left is not None:
            return left
        return None


if __name__ == "__main__":
    a = TreeNode(2)
    b = a.left = TreeNode(1)
    c = a.right = TreeNode(3)
    d = b.left = TreeNode(4)
    s = Solution()
    print(s.lowest_common_ancestor(a, b, d).val)
