from ds.modules import ListNode


class LinkedListQueue:
    """基于链表实现的队列"""
    def __init__(self):
        """初始化对头和尾部的指针"""
        self._front: ListNode | None = None
        self._rear: ListNode | None = None
        self._size: int = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, num : int):
        """入队"""
        node = ListNode(num)
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def pop(self) -> int:
        """出队"""
        val = self.peak()
        self._front = self._front.next
        self._size -= 1
        return val

    def peak(self) -> int:
        """返回队首元素"""
        if self.is_empty():
            raise ValueError("队列为空")
        return self._front.val

    def to_list(self) -> list[int]:
        """转化为列表用于打印"""
        queue = []
        temp = self._front
        while temp:
            queue.append(temp.val)
            temp = temp.next
        return queue