from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 1. 求链表长度并找到尾节点
        length, tail = 1, head
        while tail.next:
            length += 1
            tail = tail.next

        # 2. k % length, 找到对应位置
        k = k % length
        if k == 0:
            return head

        # 3. 成环
        tail.next = head

        # 4. 找到新的尾节点(正着数 length - k 个)
        steps = length - k
        for _ in range(steps):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head
