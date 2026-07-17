# Last updated: 7/17/2026, 11:58:07 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        
        tracker = {}
        for num in nums:
            if num in tracker:
                tracker[num] += 1
            else:
                tracker[num] = 1

        # Find the element that appears more than len(nums) // 2 times
        return max(tracker, key=tracker.get)
        


