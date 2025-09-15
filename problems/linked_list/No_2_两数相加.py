# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例 1：

# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.

# 示例 2：
# 输入：l1 = [0], l2 = [0]
# 输出：[0]

# 示例 3：
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]

# 提示：

# 每个链表中的节点数在范围 [1, 100] 内
# 0 <= Node.val <= 9
# 题目数据保证列表表示的数字不含前导零
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 哑头节点，简化边界处理
        dummy = ListNode(0)
        cur = dummy
        carry = 0  # 进位

        # 只要还有数字或者还有进位就继续
        while l1 or l2 or carry:
            s = carry
            # 如果有 l1，加入
            if l1:
                s += l1.val
                l1 = l1.next
            # 如果有 l2，加入
            if l2:
                s += l2.val
                l2 = l2.next

            # 计算进位和个位
            carry, digit = divmod(s, 10)  # 分别拿到个位和新的进位
            cur.next = ListNode(digit)  # 把个位接到结果链表里
            cur = cur.next

        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(5, None))))

    res = solution.addTwoNumbers(l1, l2)
    while res:
        print(res.val)
        res = res.next
