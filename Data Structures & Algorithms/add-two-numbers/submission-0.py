# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1, idx = 0, 0
        while l1:
            num1 += l1.val * (10**idx)
            idx +=1 
            l1 = l1.next
        
        num2, idx = 0, 0
        while l2:
            num2 += l2.val * (10**idx)
            idx += 1
            l2 = l2.next
        
        res = num1 + num2
        dummy = ListNode(-1)
        curr = dummy
        for digit in str(res)[::-1]:
            new_node = ListNode(int(digit))
            curr.next = new_node
            curr = curr.next
        return dummy.next
