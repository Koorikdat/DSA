# Last updated: 7/20/2026, 1:37:40 PM
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        solution = ListNode()
        curr = solution
        # create an empty linked list to hold the solution
        # solution is a null head pointer, curr is our iterator



        while list1 and list2:
        # proceed only if both lists have a value
            if list1.val < list2.val:
                # check if list1 is smaller
                curr.next = list1
                list1 = list1.next
                #append the smaller number to our holder bc we're ascending
            else:
                curr.next = list2
                list2 = list2.next
                # same logic but checks if list2 value is smaller

            curr = curr.next
            # iterate curr to whatever is the next number we found in previous block

        # if one list is empty, automatically we must pull from the other
        if list1 is not None:
            curr.next = list1
        else:
            curr.next = list2

        # return the second value of the solution linked list bc first is a null value 
        return solution.next 