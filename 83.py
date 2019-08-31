# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        q = head
        while p != None and q != None and q.next != None:
            p = p.next
            q = q.next
            q = q.next
            if p == q:
                return True
        return False
        
# ---------- 56ms, 11.9MB ----------- #