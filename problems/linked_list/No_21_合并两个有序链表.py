# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例 1：
#
#
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：
#
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
# 提示：
#
# 两个链表的节点数目范围是 [0, 50]
# -100 <= Node.val <= 100
# l1 和 l2 均按 非递减顺序 排列
#
# Related Topics
# 递归
# 链表


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode(0, None)

        dummy = res

        # 同时遍历 list1 和 list2，比较当前位置的值，小的值插入到 res 后面，最后哪个没有遍历完，直接接到 res 后
        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next

            res = res.next

            if list1:
                res.next = list1

            if list2:
                res.next = list2

        return dummy.next


if __name__ == "__main__":
    # 构造两个链表
    list1 = ListNode(1, (ListNode(2, ListNode(4, None))))
    list2 = ListNode(1, (ListNode(3, ListNode(4, None))))

    sol = Solution()
    merged = sol.mergeTwoLists(list1, list2)

    # 输出测试
    while merged:
        print(merged.val)
        merged = merged.next
