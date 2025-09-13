from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        # 把新节点插在原节点后面： 1 → 1' → 2 → 2' → …
        cur = head
        while cur:
            nxt = cur.next
            copy = Node(cur.val, nxt, None)  # 先不管 random
            cur.next = copy
            cur = nxt

        # 给新节点的 random 赋值：copy.random = origin.random.next
        cur = head
        while cur:
            if cur.random:               # 原节点有 random
                cur.next.random = cur.random.next
            cur = cur.next.next          # 跳过刚才插入的 copy

        # 把两条链表拆开，恢复原链表并拿到新链表头
        cur, new_head = head, head.next
        while cur:
            copy = cur.next
            cur.next = copy.next         # 恢复原链表
            if copy.next:                # 让新链表也串起来
                copy.next = copy.next.next
            cur = cur.next
        return new_head


if __name__ == "__main__":
    solution = Solution()

    # 1. 手动构造链表 7→13→11→10→1，random 指向如题目示例
    nodes = [Node(7), Node(13), Node(11), Node(10), Node(1)]
    for i in range(4):
        nodes[i].next = nodes[i + 1]

    nodes[1].random = nodes[0]   # 13→7
    nodes[2].random = nodes[4]   # 11→1
    nodes[3].random = nodes[2]   # 10→11
    nodes[4].random = nodes[0]   # 1→7
    # nodes[0].random 默认 None

    # 2. 调用算法
    new_head = solution.copyRandomList(nodes[0])

    # 3. 打印验证：先按 next 顺序输出 val 和 random 的 val
    cur = new_head
    print("next 顺序：", end="")
    while cur:
        r_val = cur.random.val if cur.random else "None"
        print(f"{cur.val}({r_val})", end=" → " if cur.next else "\n")
        cur = cur.next
