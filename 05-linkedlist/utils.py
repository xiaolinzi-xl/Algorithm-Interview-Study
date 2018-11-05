class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createLinkedList(arr):
    if len(arr) == 0:
        return None

    head = ListNode(arr[0])
    cur = head

    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next

    return head


def printLinkedList(head):
    cur = head

    while cur != None:
        print(str(cur.val) + '->', end='')
        cur = cur.next
    print('NULL')
