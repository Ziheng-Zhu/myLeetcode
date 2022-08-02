
# 给定一个链表，判断链表中是否有环。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，
# 则链表中存在环。 为了表示给定链表中的环，
# 我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。
# 注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#
# 如果链表中存在环，则返回 true 。 否则，返回 false 。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 使用哈希表，遍历所有节点，每次遍历一个节点，判断该节点是否被访问过
    def hasCycle(self, head: ListNode) -> bool:
        # 换成list也行
        seen = set()
        while head:
            if head in seen:
                return True
            # 对应的这里要换成seen.append()
            seen.add(head)
            head = head.next
        return False

    # Floyd判圈算法
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow!=fast:
            # 不存在在环的情况
            if not fast or not fast.next:
                return False
            # 慢指针每次移动一格，快指针每次移动两格
            slow = slow.next
            fast = fast.next.next
        return True


