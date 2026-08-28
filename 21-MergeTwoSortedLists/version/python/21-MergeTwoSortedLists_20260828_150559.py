# Last updated: 8/28/2026, 3:05:59 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8
9        head = ListNode()
10        pointerNode = head
11
12        while list1 and list2:
13            if list1.val < list2.val:
14                pointerNode.next = list1
15                list1 = list1.next
16            else:
17                pointerNode.next = list2
18                list2 = list2.next
19            
20            pointerNode = pointerNode.next
21
22        if list1 and not list2:
23            pointerNode.next = list1
24            list1.next
25
26        if list2 and not list1:
27            pointerNode.next = list2
28            list2.next
29
30        return head.next
31        
32        
33
34
35
36
37    