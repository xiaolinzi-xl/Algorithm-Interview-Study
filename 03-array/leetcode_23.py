# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeKLists(self, lists):
        k = len(lists)
        vir_node = ListNode(0)
        cur_node = vir_node
        index = [i for i in range(k)]
        while len(index) > 0:
            min_val = 1 << 63
            min_index = -1
            for i in index:
                if lists[i] is not None and lists[i].val < min_val:
                    min_val = lists[i].val
                    min_index = i
            if min_index == -1:
                break
            lists[min_index] = lists[min_index].next
            if lists[min_index] is None:
                index.remove(min_index)

            cur_node.next = ListNode(min_val)
            cur_node = cur_node.next
        return vir_node.next

    def mergeKLists_1(self, lists):
        arr = []
        for i in range(len(lists)):
            while lists[i] is not None:
                arr.append(lists[i].val)
                lists[i] = lists[i].next
        arr.sort()
        vir_node = ListNode(0)
        cur_node = vir_node
        for ele in arr:
            cur_node.next = ListNode(ele)
            cur_node = cur_node.next
        return vir_node.next
