# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

# 示例 1：

# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
# 示例 2：

# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]

# 提示：
# 链表中的节点数目为 n
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000

# 进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head:
            return head

        # 工具：反转区间 [start, end] 并返回新的头与尾
        def reverse(start: ListNode, end: ListNode):
            # end 是下一段的头，反转后应变成尾
            prev, curr = end, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev  # 新头

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy  # 上一段的尾巴

        while True:
            # 1. 检查剩余长度是否足够 k
            tail = prev_group_tail
            for _ in range(k):
                tail = tail.next
                if not tail:  # 不足 k，直接结束
                    return dummy.next

            # 2. 记录下一个组的头部
            next_group_head = tail.next

            # 3. 反转当前组 [prev_group_tail.next, tail]
            new_head = reverse(prev_group_tail.next, next_group_head)

            # 4. 把反转后的子链重新接回主链
            old_head = prev_group_tail.next  # 反转前的头，现在是尾
            prev_group_tail.next = new_head  # 前驱指向新头
            old_head.next = next_group_head  # 新尾指向下一组头

            # 5. 移动 prev_group_tail 到当前组的新尾（old_head）
            prev_group_tail = old_head


if __name__ == "__main__":
    # 构造两个链表
    list1 = ListNode(1, (ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))

    sol = Solution()
    res = sol.reverseKGroup(list1, 3)

    # 输出测试
    while res:
        print(res.val)
        res = res.next
