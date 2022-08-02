# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 递归
    def reverseList(self, head: ListNode) -> ListNode:
        # not head 是防止空链表，
        # not head.next 表示的是参数已经是链表最后一个了，可以直接范围
        if not head or not head.next:
            return head
        # 向子问题要答案，也就是说当前节点之后的节点都已经完成了反转
        reverse_head = self.reverseList(head.next)
        # 当前节点之后的下一个节点需要指向自身
        head.next.next = head
        # 同时要去掉当前节点指向下一个节点
        head.next = None
        return reverse_head

    # 双指针
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev