# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        head = ListNode(0)
        head.next = None
        H = head
        while p != None and q != None:
            if p.val < q.val:
                H.next = p
                H = H.next
                p = p.next
            else:
                H.next = q
                H = H.next
                q = q.next
        
        while p != None:
            H.next = p
            H = H.next
            p = p.next
        
        while q != None:
            H.next = q
            H = H.next
            q = q.next
        
        return head.next
# ----------- 56ms, 14MB ----------#