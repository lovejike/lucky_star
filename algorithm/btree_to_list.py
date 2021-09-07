# 2tree -> list
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # 递归调用
        self.flatten(root.left)
        self.flatten(root.right)

        # 后序遍历：左-右-根
        # 左右子树拉平成链表
        left = root.left
        right = root.right

        # 左子树作为右子树
        root.left = None
        root.right = left

        # 原先右子树接到当前右子树末端
        p = root
        # 找到当前右子树末端
        while p.right is not None:
            p = p.right
        p.right = right

    def tree_2_list(self, root):
        if not root:
            return
        res = []
        while root:
            res.append(root.val)
            root = root.right
        return res


if __name__ == '__main__':
    nodelist = [TreeNode(i) for i in [1, 2, 3, 4]]
    nodelist[0].left = nodelist[1]
    nodelist[0].right = None
    nodelist[1].right = nodelist[3]
    nodelist[1].left = nodelist[2]
    root = nodelist[0]
    s = Solution()
    s.flatten(root)
    print(s.tree_2_list(root))



