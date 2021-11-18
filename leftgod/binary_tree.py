class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTreeRecur:
    def __init__(self):
        pass

    def pre_order(self, root, result):
        if not root:
            return
        # print("pre-order: ")
        # print(root.val)
        result.append(root.val)
        self.pre_order(root.left, result)
        self.pre_order(root.right, result)
        return result

    def in_order(self, root, result):
        if not root:
            return
        # print("in-order: ")
        self.in_order(root.left, result)
        result.append(root.val)
        self.in_order(root.right, result)
        return result

    def post_order(self, root, result):
        if not root:
            return
        # print("post-order: ")
        self.post_order(root.left, result)
        self.post_order(root.right, result)
        result.append(root.val)
        return result


class BinaryTreeNoRecur:
    def __init__(self):
        pass

    def pre_order(self, root):
        if not root:
            return
        res = []
        stack = []
        stack.append(root)
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
        while root:
            stack.append(root)
            root = root.left
        while stack:
            tmp = stack.pop()
            if tmp:
                res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
        return res

    def post_order(self, root):
        if not root:
            return
        res = []
        stack1 = []
        stack2 = []
        stack1.append(root)
        while stack1:
            tmp = stack1.pop()
            if tmp:
                stack2.append(tmp)
            if tmp.left:
                # res.append(tmp.val)
                stack1.append(tmp.left)
            if tmp.right:
                stack1.append(tmp.right)
        while stack2:
            res.append(stack2.pop().val)
        return res



if __name__ == "__main__":
    tree_node = [TreeNode(i) for i in range(5)]
    tree_node[0].left = tree_node[1]
    tree_node[0].right = tree_node[2]
    tree_node[1].left = tree_node[3]
    tree_node[1].right = tree_node[4]
    s = BinaryTreeRecur()
    res1 = []
    res2 = []
    res3 = []
    # print(s.pre_order(tree_node[0], res1))
    # print(s.in_order(tree_node[0], res2))
    # print(s.post_order(tree_node[0], res3))

    sr = BinaryTreeNoRecur()
    print(sr.pre_order(tree_node[0]))
    print(sr.in_order(tree_node[0]))
    print(sr.post_order(tree_node[0]))