# Last updated: 7/22/2026, 4:18:50 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        
9        solution = ListNode()
10        pointer = solution
11
12        while list1 and list2:
13            if list1.val <= list2.val:
14                pointer.next = list1
15                list1 = list1.next
16                pointer = pointer.next
17
18            elif list2.val < list1.val:
19                pointer.next = list2
20                list2 = list2.next
21                pointer = pointer.next
22
23
24        if list1:
25            pointer.next = list1
26        else:
27            pointer.next = list2
28        
29        return solution.next
30
31
32