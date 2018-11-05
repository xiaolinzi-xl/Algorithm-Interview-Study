# Definition for singly-linked list.
from utils import ListNode, createLinkedList, printLinkedList


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


def main():
    arr = [1, 2, 3, 4, 5]
    head = createLinkedList(arr)
    printLinkedList(head)

    head = Solution().reverseList(head)
    printLinkedList(head)


if __name__ == '__main__':
    main()
