# Last updated: 7/17/2026, 3:27:16 PM
1class Solution:
2    def isMonotonic(self, nums: List[int]) -> bool:
3        increasing = True
4        decreasing = True
5
6        for i in range(len(nums) - 1):
7            if nums[i] > nums[i + 1]:
8                increasing = False
9            if nums[i] < nums[i + 1]:
10                decreasing = False
11
12        return increasing or decreasing
13