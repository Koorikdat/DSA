# Last updated: 8/7/2026, 4:41:34 PM
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
16        #progress if there is a next element or a carry (Typically 0).
17        #We don't care about reverse order because you add from right to left anyway
18        while l1 or l2 or carry:
19            total = carry
20
21            if l1:
22                total += l1.val
23                l1 = l1.next
24
25            if l2:
26                total += l2.val
27                l2 = l2.next
28
29            # We are using the last digit for input
30            num = total % 10
31
32            # Remembering the first digit for carrying 
33            carry = total // 10
34
35            dummy.next = ListNode(num)
36            dummy = dummy.next
37
38        return res.next