# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        len = 0
        p = head
        while p != None:
            len += 1
            p = p.next

        pos = int(len / 2)
            
        p = head
        for i in range(pos):
            p = p.next
        print(p.val)
        return p
# ---------- 40ms, 13.9MB ---------- #