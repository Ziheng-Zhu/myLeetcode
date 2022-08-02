# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
# 进阶：你能尝试使用一趟扫描实现吗？

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    # 运用双指针+dummy链表
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0,head)
        slow = dummy
        fast = head
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next



        # p1 =   head
        # fast = p2 = p1.next
        # while n>0 and fast:
        #     fast = fast.next
        #     n -=1
        #
        # while fast:
        #     p1 = p1.next
        #     p2 = p2.next
        #     fast = fast.next
        # if p1 and p2:
        #     p1.next = p2.next
        # return head

    # 回溯法后序遍历
    def removeNthFromEnd(self,head,n):
        traverse = traverse(head,n)
        if traverse==n:
            return head.next
        return head

    def traverse(self,node,n):
        if not node:
            return 0
        num = traverse(node.next,n)
        if num==n:
            node.next = node.next.next

        return num + 1