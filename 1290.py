# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        len = 0
        p = head
        while p != None:
            p = p.next
            len += 1
        ans = 0
        p = head
        len -= 1
        while p != None:
            ans += pow(2, len) * p.val
            p = p.next
            len -= 1
        return ans