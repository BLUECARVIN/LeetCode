# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        len = 0
        p = head
        while p != None:
            p = p.next
            len += 1
        len = len - k 
        p = head
        while len > 0:
            p = p.next
            len -= 1
        return p.val