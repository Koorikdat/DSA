# Last updated: 7/17/2026, 11:58:03 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        for x in nums:
            if x == 0:
                nums.remove(x)
                nums.append(0)

    
        """
        Do not return anything, modify nums in-place instead.
        """