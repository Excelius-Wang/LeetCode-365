from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy.next
        sml_list = list()
        big_list = list()
        # 直接放到两个列表里即可
        while cur:
            if cur.val < x:
                sml_list.append(ListNode(cur.val, None))
            else:
                big_list.append(ListNode(cur.val, None))
            cur = cur.next
        dummy = res = ListNode(0, None)
        for i in range(len(sml_list)):
            res.next = sml_list[i]
            res = res.next
        for i in range(len(big_list)):
            res.next = big_list[i]
            res = res.next
        return dummy.next
