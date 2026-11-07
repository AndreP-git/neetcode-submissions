# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # [0, 1, 2, 3, 4, 5, 6]
        # [0, 1, 2, 3, 6, 5, 4]
        # curr=0, tmp=1, next=6
        # [0 -> 6 -> ]
        # curr=6, tmp=5, next=1
        # [0 -> 6 -> 1]
        # curr=1, tmp=2, next=5
        # ... (while tmp != None)

        # step 0: find mid list
        curr = head
        mid = head
        while curr and curr.next:
            curr = curr.next.next
            mid = mid.next
        
        # step 1: reverse second half
        curr = mid.next
        mid.next = None
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # step 2: modify list in place
        curr = head
        next_node = prev
        while next_node:
            tmp = curr.next
            curr.next = next_node
            curr = next_node
            next_node = tmp

