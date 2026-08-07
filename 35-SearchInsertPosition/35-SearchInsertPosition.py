# Last updated: 8/6/2026, 11:15:28 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # just a binary search implementation for log(n)
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left