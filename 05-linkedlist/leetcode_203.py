from utils import ListNode, createLinkedList, printLinkedList


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        vir_head = ListNode(0)
        vir_head.next = head

        pre = vir_head
        cur = pre.next

        while cur != None:
            if cur.val == val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre.next = cur
                pre = cur
                cur = cur.next

        return vir_head.next

    def removeElements_2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        vir_head = ListNode(0)
        vir_head.next = head

        cur = vir_head

        while cur.next != None:
            if cur.next.val == val:
                delNode = cur.next
                cur.next = delNode.next
                delNode.next = None
            else:
                cur = cur.next

        return vir_head.next


def main():
    arr = [1, 2, 6, 3, 4, 5, 6]
    head = createLinkedList(arr)
    printLinkedList(head)

    head = Solution().removeElements_2(head, 6)
    printLinkedList(head)


if __name__ == '__main__':
    main()
