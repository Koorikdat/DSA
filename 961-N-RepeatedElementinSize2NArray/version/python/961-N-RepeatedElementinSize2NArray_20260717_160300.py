# Last updated: 7/17/2026, 4:03:00 PM
1class Solution:
2    def repeatedNTimes(self, nums: List[int]) -> int:
3
4
5        n = len(nums) // 2
6
7        seen = {}
8        for i in range(0, len(nums)):
9            if nums[i] in seen:
10                seen[nums[i]] += 1
11            else:
12                seen[nums[i]] = 1  
13
14        for element, frequency in seen.items(): 
15            if frequency == n: 
16                return element