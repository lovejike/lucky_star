class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def btree_2_list(self, root):
        if root is None:
            return root
        tmp_arr = []
        res_arr = []
        p = root
        # 中序遍历
        while tmp_arr or p:
            if p:
                tmp_arr.append(p)
                p = p.left
            else:
                node = tmp_arr.pop()
                print(node.val)
                res_arr.append(node)
                p = node.right

        # 双向链表
        result = res_arr[0]
        while res_arr:
            tmp = res_arr.pop()
            if res_arr:
                tmp.left = res_arr[0]
                res_arr[0].right = tmp

        return result


if __name__ == '__main__':
    nodelist = [TreeNode(i) for i in [1, 2, 3, 4]]
    nodelist[0].left = nodelist[1]
    nodelist[0].right = None
    nodelist[1].right = nodelist[3]
    nodelist[1].left = nodelist[2]
    root = nodelist[0]
    s = Solution()
    res = s.btree_2_list(root)

