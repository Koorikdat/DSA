class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:


        n = len(nums) // 2

        seen = {}
        for i in range(0, len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1  

        for element, frequency in seen.items(): 
            if frequency == n: 
                return element