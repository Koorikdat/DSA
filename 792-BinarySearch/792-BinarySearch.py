# Last updated: 7/17/2026, 11:57:55 AM
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        floor =  0
        ceiling = len(nums)-1

        while floor <= ceiling:
            mid = (floor + ceiling) // 2


            if nums[mid] == target:
                return mid


            if nums[mid] < target:
                floor = mid + 1

                
            else:
                ceiling = mid - 1 

        return -1
        