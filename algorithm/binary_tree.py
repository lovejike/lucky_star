class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorder(self, root, res=[]):
        if not root:
            return
        res.append(root.val)
        if root.left is not None:
            self.preorder(root.left, res)
        if root.right is not None:
            self.preorder(root.right, res)
        return res

    def inorder(self, root, res=[]):
        if not root:
            return
        if root.left is not None:
            self.preorder(root.left, res)
        res.append(root.val)
        if root.right is not None:
            self.preorder(root.right, res)
        return res

    def postorder(self, root, res=[]):
        if not root:
            return
        if root.left:
            self.postorder(root.left, res)
        if root.right:
            self.postorder(root.right, res)
        res.append(root.val)
        return res


class IterSolution:
    def preorder(self, root):
        if not root:
            return
        stack = [root]
        res = []
        while stack:
            tmp = stack.pop()
            if tmp:
                res.append(tmp.val)
                stack.append(tmp.right)
                stack.append(tmp.left)
        return res

    def inorder(self, root):
        if not root:
            return
        stack = []
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def postorder(self, root):
        if not root:
            return
        stack = []
        res = []
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
    # 层序遍历
    def bfs(self, root):
        if not root:
            return
        res = []
        queue = [root]
        while queue:
            len_q = len(queue)
            for i in range(len_q):
                q = queue.pop(0)
                if q:
                    res.append(q.val)
                    queue.append(q.left if q.left else None)
                    queue.append(q.right if q.right else None)
        return res


# binary tree所有节点值加一
def plus_one(root):
    if not root:
        return
    root.val += 1
    plus_one(root.left)
    plus_one(root.right)


# 两个binary tree是否相等
def is_same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)

# binary search tree合法性
def isvalidBST(root):
    return isvalid2BST(root, None, None)

# 如果是左子树，那么最大值是root，最小值是空；如果是右子树，最大值是空，最小值是root
def isvalid2BST(root, min, max):
    if not root:
        return True
    if min is not None and min.val >= root.val:
        return False
    if max is not None and max.val <= root.val:
        return False
    return isvalid2BST(root.left, min, root) and isvalid2BST(root.right, root, max)

# 插入一个值
def insert_value(root, value):
    if not root:
        return TreeNode(value)
    if root.val > value:
        root.left = insert_value(root.left, value)
    if root.val < value:
        root.right = insert_value(root.right, value)
    return root


# 判断BST中是否存在一个数
def isinBST(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    if root.val > target:
        return isinBST(root.left, target)
    if root.val < target:
        return isinBST(root.right, target)


if __name__ == "__main__":
    l1 = TreeNode(1)
    l2 = TreeNode(3)
    l3 = TreeNode(4)
    l4 = TreeNode(5)
    l1.left = l2
    l1.right = l3
    l2.right = l4
    s = Solution()
    print(s.preorder(l1))
    print(s.inorder(l1))
    print(s.postorder(l1))
    print("------")
    s1 = IterSolution()
    print(s1.preorder(l1))
    print(s1.inorder(l1))
    print(s1.postorder(l1))
    print(s1.bfs(l1))

    r1 = TreeNode(6)
    r1.left = l2
    r2 = TreeNode(1)
    r2.right = l2
    # print(is_same_tree(r1,r2))
    print(isvalidBST(r1))
    print(isinBST(r1, 4))
    res = insert_value(r1, 9)
    print(res.val, res.left.val, res.right.val)
