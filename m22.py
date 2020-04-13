# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        l = 0
        p = head
        while p:
            l += 1
            p = p.next
        l -= k
        p = head
        while l:
            l -= 1
            p = p.next
        return p