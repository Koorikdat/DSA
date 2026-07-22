# Last updated: 7/22/2026, 4:29:20 PM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3
4        index = 0
5        for i in range(0, len(nums)):
6            if nums[i] != val:
7                nums[index] = nums[i]
8                index += 1
9
10        return index