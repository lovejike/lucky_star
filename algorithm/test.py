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
    # 全部
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





















