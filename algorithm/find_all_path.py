class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self._one_path = []
        self._total_res = []

    # 二叉树给定和的所有路径
    def find_all_path(self, root, target_num):
        # 判断空的二叉树情况
        if root is None:
            return self._total_res
        self._one_path.append(root.val)
        target_num -= root.val
        if target_num == 0 and root.left is None and root.right is None:
            self._total_res.append(self._one_path[:])
        elif target_num > 0:
            self.find_all_path(root.left, target_num)
            self.find_all_path(root.right, target_num)
        self._one_path.pop()
        return self._total_res

    # 打印二叉树的所有路径
    def binaryTreePaths(self, root):
        def get_paths(root, path, res):
            if root:
                path.append(str(root.val))
                left = get_paths(root.left, path, res)
                right = get_paths(root.right, path, res)
                if not left and not right:                  # 如果root是叶子结点
                    res.append("->".join(path))             # 把当前路径加入到结果列表中
                path.pop()                                  # 返回上一层递归时，要让当前路径恢复原样
                return True

        res = []
        get_paths(root, [], res)
        return res


if __name__ == '__main__':
    nodelist = [BinaryTreeNode(i) for i in [4, 2, 7, 8, 3]]
    nodelist[0].left = nodelist[1]
    nodelist[0].right = nodelist[2]
    nodelist[1].left = nodelist[3]
    nodelist[1].right = nodelist[4]
    root = nodelist[0]
    s = Solution()
    print(s.find_all_path(root, 11))
    print(s.binaryTreePaths(root))
