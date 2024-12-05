from python_hello算法.modules import TreeNode


def pre_order(root: TreeNode):
    """前序遍历：例题二"""
    if root is None:
        return
    # 尝试
    path = []
    res = []
    path.append(root)
    if root.val == 7:
        # 记录解
        res.append(list(path))
    pre_order(root.left)
    pre_order(root.right)
    # 回退
    path.pop()
    return res