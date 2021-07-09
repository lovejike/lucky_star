# 二叉搜索树满足左子树的值<根结点的值<右子树的值，所以对二叉树进行中序遍历，然后对每个结点进行双向链接。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        p = pRootOfTree
        arr = []
        resarr = []
        # 中序遍历
        while p or arr:
            if p:
                arr.append(p)
                p = p.left
            else:
                node = arr.pop()
                resarr.append(node)
                p = node.right
        # 双向链接
        res = resarr[0]
        while resarr:
            tmp = resarr.pop(0)
            if resarr:
                tmp.right = resarr[0]
                resarr[0].left = tmp
        return res


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     def Convert(self, root):
#         if not root:
#             return None
#         if not root.left and not root.right:
#             return root
#
#         # 将左子树构建成双链表，返回链表头
#         left = self.Convert(root.left)
#         p = left
#
#         # 定位至左子树的最右的一个结点
#         while left and p.right:
#             p = p.right
#
#         # 如果左子树不为空，将当前root加到左子树链表
#         if left:
#             p.right = root
#             root.left = p
#
#         # 将右子树构造成双链表，返回链表头
#         right = self.Convert(root.right)
#         # 如果右子树不为空，将该链表追加到root结点之后
#         if right:
#             right.left = root
#             root.right = right
#
#         return left if left else root
