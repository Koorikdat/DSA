# Last updated: 7/20/2026, 1:37:00 PM
1class Solution:
2    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
3
4        solution = ListNode()
5        curr = solution
6        # create an empty linked list to hold the solution
7        # solution is a null head pointer, curr is our iterator
8
9
10
11        while list1 and list2:
12        # proceed only if both lists have a value
13            if list1.val < list2.val:
14                # check if list1 is smaller
15                curr.next = list1
16                list1 = list1.next
17                #append the smaller number to our holder bc we're ascending
18            else:
19                curr.next = list2
20                list2 = list2.next
21                # same logic but checks if list2 value is smaller
22
23            curr = curr.next
24            # iterate curr to whatever is the next number we found in previous block
25
26        # if one list is empty, automatically we must pull from the other
27        if list1 is not None:
28            curr.next = list1
29        else:
30            curr.next = list2
31
32        # return the second value of the solution linked list bc first is a null value 
33        return solution.next 