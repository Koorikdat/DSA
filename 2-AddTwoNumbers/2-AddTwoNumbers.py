# Last updated: 8/6/2026, 11:15:41 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Set up linked list, res points at head, dummy iterates
        dummy = ListNode()
        res = dummy

        # track the carry over as well as the result of each digits addition
        total = carry = 0

        #progress if there is a next element or a carry (Typically 0).
        #We don't care about reverse order because you add from right to left anyway
        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            # We are using the last digit for input
            num = total % 10

            # Remembering the first digit for carrying 
            carry = total // 10

            dummy.next = ListNode(num)
            dummy = dummy.next

        return res.next