from python_hello算法.modules import TreeNode


def pre_order(root: TreeNode):
    """前序遍历：例题一"""
    res = []
    if root is None:
        return
    if root.val == 7:
        # 记录解
        res.append(root)
    pre_order(root.left)
    pre_order(root.right)
    return res