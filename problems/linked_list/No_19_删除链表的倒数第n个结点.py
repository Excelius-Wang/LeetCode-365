from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        这个题解的思路是，把所有的节点都放到一个列表里，然后这样就可以按照下标进行操作了
        """
        dummy = ListNode(0, head)
        node_list = [dummy]  # 下标 0 就是哑结点
        cur = head
        while cur:
            node_list.append(cur)
            cur = cur.next
        node_list.append(None)  # 备用

        m = len(node_list) - 2  # 实际节点个数
        # 不管删的是谁，前驱都在 node_list[m - n]
        node_list[m - n].next = node_list[m - n + 2]  # 跳过被删节点
        return dummy.next


class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        最佳题解：使用快慢指针，快指针先走 n + 1, 然后一起走，快指针走到 None, 慢指针就走到了要删除节点的前一个位置
        """
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy

        for i in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
