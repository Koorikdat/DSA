# Last updated: 7/22/2026, 2:09:14 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3
4        seen = {}
5
6        for i in range (0, len(nums)):
7            goal = target - nums[i]
8            if goal in seen:
9                return [seen[goal], i]
10            else:
11                seen[nums[i]] = i
12
13