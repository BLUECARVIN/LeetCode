# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        H = ListNode(None)
        H.next = head
        p = H
        while p != None and p.next != None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return H.next
# ---------- 84ms, 18.6MB ---------- #