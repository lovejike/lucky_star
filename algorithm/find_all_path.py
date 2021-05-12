class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self._one_path = []
        self._total_res = []

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


if __name__ == '__main__':
    nodelist = [BinaryTreeNode(i) for i in [4, 2, 7, 8, 3]]
    nodelist[0].left = nodelist[1]
    nodelist[0].right = nodelist[2]
    nodelist[1].left = nodelist[3]
    nodelist[1].right = nodelist[4]
    root = nodelist[0]
    s = Solution()
    print(s.find_all_path(root, 11))
