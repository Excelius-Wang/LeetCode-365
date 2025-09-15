# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。
# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。
# 返回复制链表的头节点。
# 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 你的代码 只 接受原链表的头节点 head 作为传入参数。

# 示例 1：
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

# 示例 2：
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]

# 示例 3：
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]

# 提示：
# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random 为 null 或指向链表中的节点。
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
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
            if cur.random:  # 原节点有 random
                cur.next.random = cur.random.next
            cur = cur.next.next  # 跳过刚才插入的 copy

        # 把两条链表拆开，恢复原链表并拿到新链表头
        cur, new_head = head, head.next
        while cur:
            copy = cur.next
            cur.next = copy.next  # 恢复原链表
            if copy.next:  # 让新链表也串起来
                copy.next = copy.next.next
            cur = cur.next
        return new_head


if __name__ == "__main__":
    solution = Solution()

    # 1. 手动构造链表 7→13→11→10→1，random 指向如题目示例
    nodes = [Node(7), Node(13), Node(11), Node(10), Node(1)]
    for i in range(4):
        nodes[i].next = nodes[i + 1]

    nodes[1].random = nodes[0]  # 13→7
    nodes[2].random = nodes[4]  # 11→1
    nodes[3].random = nodes[2]  # 10→11
    nodes[4].random = nodes[0]  # 1→7
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
