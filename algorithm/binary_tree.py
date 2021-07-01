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
