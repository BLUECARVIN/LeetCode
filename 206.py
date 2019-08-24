# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        H = ListNode(0)
        H.next = None
        p = head
        
        while p != None:
            q = ListNode(p.val)
            q.next = H.next
            H.next = q
            p = p.next
        return H.next
# ----------- 56ms, 15.0MB ----------- #