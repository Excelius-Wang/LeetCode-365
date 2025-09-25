from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        cur = head

        while cur:
            # 如果当前指针的值和下一个节点的值相等
            if cur.next and cur.val == cur.next.val:
                val = cur.val
                while cur and val == cur.val:
                    cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next

        return dummy.next
