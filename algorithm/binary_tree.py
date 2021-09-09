class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self._one_path = []
        self._all_path = []
        self._all_path_2 = []

    def pre_order(self, root):
        if not root:
            return
        res = []
        stack = [root]
        while stack:
            tmp = stack.pop()
            if tmp:
                res.append(tmp.val)
                stack.append(tmp.right)
                stack.append(tmp.left)
        return res

    def in_order(self, root):
        if not root:
            return
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            tmp = stack.pop()
            res.append(tmp.val)
            root = tmp.right
        return res

    def post_order(self, root):
        if not root:
            return
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                if root.left:
                    root = root.left
                else:
                    root = root.right
            tmp = stack.pop()
            res.append(tmp.val)
            if stack and tmp == stack[-1].left:
                root = stack[-1].right
            else:
                root = None
        return res
    def cfs(self, root):
        if not root:
            return
        res = []
        queue = [root]
        while queue:
            for i in range(len(queue)):
                tmp = queue.pop(0)
                if tmp:
                    res.append(tmp.val)
                    queue.append(tmp.left if tmp.left else None)
                    queue.append(tmp.right if tmp.right else None)
        return res

    # 路径和固定
    def find_all_path(self, root, target_num):

        if not root:
            return self._all_path
        target_num -= root.val
        self._one_path.append(root.val)
        if target_num == 0 and root.left is None and root.right is None:
            self._all_path.append(self._one_path[:])
        elif target_num > 0:
            self.find_all_path(root.left, target_num)
            self.find_all_path(root.right, target_num)
        self._one_path.pop()
        return self._all_path
    # 全部路径
    def all_tree_path(self, root):
        def get_path(root, path, res):
            if not root:
                return
            path.append(str(root.val))
            left = get_path(root.left, path, res)
            right = get_path(root.right, path, res)
            if not left and not right:
                res.append("->".join(path))
            path.pop()
            return True
        res = []
        get_path(root, [], res)
        return res

    # binary tree所有节点值加一
    def plus_one(self, root):
        if not root:
            return
        root.val += 1
        self.plus_one(root.left)
        self.plus_one(root.right)

    # 两个binary tree是否相等
    def is_same_tree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return self.is_same_tree(root1.left, root2.left) and self.is_same_tree(root1.right, root2.right)

    # binary search tree合法性
    def isvalidBST(self, root):
        return self.isvalid2BST(root, None, None)

    # 如果是左子树，那么最大值是root，最小值是空；如果是右子树，最大值是空，最小值是root
    def isvalid2BST(self, root, min, max):
        if not root:
            return True
        if min is not None and min.val >= root.val:
            return False
        if max is not None and max.val <= root.val:
            return False
        return self.isvalid2BST(root.left, min, root) and self.isvalid2BST(root.right, root, max)

    # 插入一个值
    def insert_value(self, root, value):
        if not root:
            return TreeNode(value)
        if root.val > value:
            root.left = self.insert_value(root.left, value)
        if root.val < value:
            root.right = self.insert_value(root.right, value)
        return root

    # 判断BST中是否存在一个数
    def isinBST(self, root, target):
        if not root:
            return False
        if root.val == target:
            return True
        if root.val > target:
            return self.isinBST(root.left, target)
        if root.val < target:
            return self.isinBST(root.right, target)

    # 二叉树转换为单链表
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

    # 二叉树转换为双向链表
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

    # 二叉树最近公共祖先
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
    tns = [TreeNode(i+1) for i in range(4)]
    tns[0].left = tns[3]
    tns[0].right = tns[1]
    tns[1].right = tns[2]
    s = Solution()
    # import pdb
    # pdb.set_trace()
    print(s.pre_order(tns[0]))
    print(s.in_order(tns[0]))
    print(s.post_order(tns[0]))
    print(s.cfs(tns[0]))
    print(s.find_all_path(tns[0], 6))
    print(s.all_tree_path(tns[0]))





















