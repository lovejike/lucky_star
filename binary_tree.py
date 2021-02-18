# 定义节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前序遍历（递归）
def preorder_rec(root):
    res = []
    if not root:
        return
    #print(root.val)
    res.append(root.val)
    if root.left:
        res.extend(preorder_rec(root.left))
    if root.right:
        res.extend(preorder_rec(root.right))
    return res


# 前序遍历（迭代）
def preorder_iter(root):
    if not root:
        return
    stack = [root]
    res = []
    while stack:
        s = stack.pop()
        if s:
            # print(s.val)
            res.append(s.val)
            stack.append(s.right)
            stack.append(s.left)
    return res


# 中序遍历（递归）
def inorder_rec(root):
    if not root:
        return
    res = []
    if root.left:
        res.extend(inorder_rec(root.left))
    res.append(root.val)
    if root.right:
        res.extend(inorder_rec(root.right))
    return res


# 中序遍历（迭代）
def inorder_iter(root):
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


# 后序遍历（递归）
def postorder_rec(root):
    if not root:
        return
    res = []
    if root.left:
        res.extend(postorder_rec(root.left))
    if root.right:
        res.extend(postorder_rec(root.right))
    res.append(root.val)
    return res


# 后序遍历（迭代）
def postorder_iter(root):
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
        s = stack.pop()
        res.append(s.val)
        if stack and s == stack[-1].left:
            root = stack[-1].right
        else:
            root = None
    return res


# 层序遍历
def BFS(root):
    if not root:
        return
    queue = [root]
    res = []
    while queue:
        q_len = len(queue)
        for i in range(q_len):
            q = queue.pop(0)
            if q:
                res.append(q.val)
                queue.append(q.left if q.left else None)
                queue.append(q.right if q.right else None)
    return res


# 二叉树最大深度（递归）
def max_depth_rec(root):
    if not root:
        return 0
    l = 1 + max_depth_rec(root.left)
    r = 1 + max_depth_rec(root.right)
    return max(l, r)


# 二叉树最大深度（迭代）
def max_depth_iter(root):
    if not root:
        return
    stack = []
    if root:
        stack.append((1, root))
    depth = 0
    while stack:
        cur_depth, root = stack.pop()
        if root:
            depth = cur_depth if cur_depth > depth else depth
            stack.append((cur_depth+1, root.left))
            stack.append((cur_depth+1, root.right))
    return depth


# 二叉树最小深度（递归）
def min_depth_rec(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if root.left and not root.right:
        return 1 + min_depth_rec(root.left)
    if not root.left and root.right:
        return 1 + min_depth_rec(root.right)
    else:
        return 1 + min(min_depth_rec(root.left), min_depth_rec(root.right))


# 二叉树最小深度（迭代）
def min_depth_iter(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    queue = [(1, root)]
    while queue:
        cur_depth, root = queue.pop(0)
        if root.left == None and root.right == None:
            return cur_depth
        if root.left:
            queue.append((cur_depth + 1, root.left))
        if root.right:
            queue.append((cur_depth + 1, root.right))


# 二叉树的所有路径
def traverse(root):
    if not root:
        return
    if not root.left and not root.right:
        return [str(root.val)]
    left, right = [], []
    if root.left:
        left = [str(root.val) + x for x in traverse(root.left)]
    if root.right:
        right = [str(root.val) + x for x in traverse(root.right)]
    return left + right


if __name__ == '__main__':
    nodelist = [TreeNode(i) for i in [4, 2, 7, 8, 3]]
    nodelist[0].left = nodelist[1]
    nodelist[0].right = nodelist[2]
    nodelist[1].left = nodelist[3]
    nodelist[1].right = nodelist[4]
    root = nodelist[0]
    #print('二叉树根节点为：', root)
    print('前序遍历_递归:', preorder_rec(root))
    print('前序遍历_迭代:', preorder_iter(root))
    print('中序遍历_递归:', inorder_rec(root))
    print('中序遍历_迭代:', inorder_iter(root))
    print('后序遍历_递归:', postorder_rec(root))
    print('后序遍历_迭代:', postorder_iter(root))
    print('层次遍历:', BFS(root))
    print('最大深度_递归:', max_depth_rec(root))
    print('最大深度_迭代:', max_depth_iter(root))
    print('最小深度_递归:', min_depth_rec(root))
    print('最小深度_迭代:', min_depth_iter(root))
    print('所有路径:', traverse(root))

