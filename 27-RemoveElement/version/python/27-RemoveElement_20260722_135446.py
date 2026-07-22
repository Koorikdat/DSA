# Last updated: 7/22/2026, 1:54:46 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        
9        # Set up linked list, res points at head, dummy iterates
10        dummy = ListNode()
11        res = dummy
12
13        # track the carry over as well as the result of each digits addition
14        total = carry = 0
15
16        #progress if there is a next element or a carry (Typically 0)
17        while l1 or l2 or carry:
18            total = carry
19
20            if l1:
21                total += l1.val
22                l1 = l1.next
23
24            if l2:
25                total += l2.val
26                l2 = l2.next
27
28            # We are using the last digit for input
29            num = total % 10
30
31            # Remembering the first digit for carrying 
32            carry = total // 10
33
34            dummy.next = ListNode(num)
35            dummy = dummy.next
36
37        return res.next