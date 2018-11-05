# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        virnode = ListNode(0)

        pre, cur = virnode, head
        while cur != None:
            next = cur.next
            cur.next = pre.next
            pre.next = cur

            cur = next

        return virnode.next
