# Last updated: 7/23/2026, 11:12:07 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3
4        seen = {}
5
6        for i in range (0, len(nums)):
7            goal = target - nums[i]
8            if goal in seen:
9                return [i, seen[goal]]
10            else:
11                seen[nums[i]] = i
12
13