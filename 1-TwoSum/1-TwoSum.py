# Last updated: 7/20/2026, 1:37:44 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Dict = {}

        for i in range(0, len(nums)):
            key = target - nums[i]
            if key in Dict:
                return [Dict[key], i]
            else:
                Dict[nums[i]] = i
