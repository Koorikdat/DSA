# Last updated: 7/27/2026, 1:35:12 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3
4        seen = {}
5
6        for i in range(0, len(nums)):
7            key = target - nums[i]
8            if key in seen:
9                return [i, seen[key]]
10            else:
11                seen[nums[i]] = i
12
13
14
15
16