# Last updated: 7/23/2026, 11:09:36 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        seen = {}
4
5        for i in range (0, len(nums)):
6            goal = target - nums[i]
7            if goal in seen:
8                return [i, seen[goal]]
9            else:
10                seen[nums[i]] = i
11
12