# Last updated: 8/27/2026, 10:09:05 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3
4        for i in range(0, len(nums)):
5            for j in range(0, len(nums)):
6                if nums[i] + nums[j] == target and i != j:
7                    return [i, j]