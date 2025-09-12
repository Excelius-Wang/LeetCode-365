# 给你一个链表的头节点 head ，判断链表中是否有环。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
#
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。
#
#
# 示例 1：
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
# 示例 2：
#
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 示例 3：
#
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#
# 提示：
#
# 链表中节点的数目范围是 [0, 104]
# -105 <= Node.val <= 105
# pos 为 -1 或者链表中的一个 有效索引 。
#
# 进阶：你能用 O(1)（即，常量）内存解决此问题吗？
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针，快指针每次多走一步，如果相遇，则有环
        # 快指针走到末尾，则无环
        if not head:
            return False

        slow = head
        fast = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    list_node1 = ListNode(3)
    list_node2 = ListNode(2)
    list_node3 = ListNode(0)
    list_node4 = ListNode(-4)
    list_node1.next = list_node2
    list_node2.next = list_node3
    list_node3.next = list_node4
    list_node4.next = list_node2
    print(solution.hasCycle(list_node1))

    no_list_node1 = ListNode(1)
    no_list_node2 = ListNode(2)
    no_list_node3 = ListNode(3)
    no_list_node1.next = no_list_node2
    no_list_node2.next = no_list_node3
    print(solution.hasCycle(no_list_node1))
