from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 哑头节点，简化边界处理
        dummy = ListNode(0)
        cur = dummy
        carry = 0   # 进位

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
            carry, digit = divmod(s, 10)   # 分别拿到个位和新的进位
            cur.next = ListNode(digit)     # 把个位接到结果链表里
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
