# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
#
# 示例 1：
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
# 示例 2：
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
# 提示：
# 链表中节点数目为 n
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
# 进阶： 你可以使用一趟扫描完成反转吗？
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
整体思路借助头插法, 先定位到需要反转的位置的前一个位置 pre,
然后把需要插入的位置依次按照头插法的方式插入到 pre 节点后方即可.
头插法时需要注意顺序:
先保存 cur.next, 然后把 nxt 从原位置摘下，把 nxt 插入到区间最前面, 最后更新区间头指针
"""

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 如果链表为空或者不需要反转
        if not head or left == right:
            return head

        # 创建一个 pre 节点，pre 方便定位需要反转位置的前一个节点
        dummy = ListNode(0, head)
        pre = dummy
        for i in range(left - 1):
            pre = pre.next

        # 创建 cur 节点，代表当前位置
        cur = pre.next
        for i in range(right - left):
            nxt = cur.next          # 保存下一个要移动的节点
            cur.next = nxt.next     # 把 nxt 从原位置摘下
            nxt.next = pre.next     # 把 nxt 插到区间最前面
            pre.next = nxt          # 更新区间头指针

        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    res = solution.reverseBetween(l1, 2, 4)

    while res:
        print(res.val)
        res = res.next
