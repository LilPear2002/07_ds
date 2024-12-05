
class ListNode:
    # 定义链表节点结构
    def __init__(self, val):
        self.val : int = val
        self.next : ListNode | None = None


# 初始化链表
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)
# 构建节点之间的引用
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4


# 插入节点
def insert(n0: ListNode, P: ListNode):
    """在链表的节点 n0 之后插入节点 P"""
    n1 = n0.next
    P.next = n1
    n0.next = P

# 删除节点
def remove(n0: ListNode):
    """删除链表的节点 n0 之后的首个节点"""
    if not n0.next:
        return
    # n0 -> P -> n1
    P = n0.next
    n1 = P.next
    n0.next = n1

# 访问节点
def access(head: ListNode, index: int) -> ListNode | None:
    """返回链表中第 index 个节点，如果 index 超出了链表的长度，返回 None"""
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head

# 查找节点
def find(head : ListNode , target : int) -> int:
    """返回链表中第一个值为 target 的节点的索引，如果不存在，返回 -1"""
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1