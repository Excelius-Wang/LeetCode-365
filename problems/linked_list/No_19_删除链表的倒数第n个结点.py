# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_list = list()
        cur = head
        num = 0
        while cur:
            node_list.append(cur)
            num += 1
            cur = cur.next

        if num == 1:
            return

        # 删除倒数第 n 个
        pre = node_list[num - n - 1]
        need_deleted = node_list[num - n]
        nxt = node_list[num - n + 1]
        pre.next = nxt
        return head