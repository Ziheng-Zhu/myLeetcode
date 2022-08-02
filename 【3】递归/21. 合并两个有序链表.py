# 将两个升序链表合并为一个新的 升序 链表并返回。
# 新链表是通过拼接给定的两个链表的所有节点组成的。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # 递归
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
    # 这个递归用的太秀了！值得经常拿出来看看！

    # 利用虚拟头节点
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        p = dummy
        while l1 and l2:
            if l1.val > l2.val:
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next
        if not l1:
            p.next = l2
        elif not l2:
            p.next = l1
        return dummy.next
