# Last updated: 7/21/2026, 2:58:58 PM
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3
4        # just a binary search implementation for log(n)
5        left = 0
6        right = len(nums) - 1
7
8        while left <= right:
9            mid = (left + right) // 2
10
11            if nums[mid] == target:
12                return mid
13            elif nums[mid] > target:
14                right = mid - 1
15            else:
16                left = mid + 1
17        
18        return left