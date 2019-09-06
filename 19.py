# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        len = 0
        H = ListNode(None)
        H.next = head
        p = H
        while p != None:
            p = p.next
            len += 1
            
        if len == 0 or len == 1:
            return None
        
        step = len - n - 1
        p = H
        for i in range(step):
            p = p.next
        print(p.val)
        p.next = p.next.next
        
        return H.next
# ----------- 60ms, 13.8MB ---------- #