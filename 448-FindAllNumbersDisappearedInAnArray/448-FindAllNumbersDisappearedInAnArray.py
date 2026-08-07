# Last updated: 8/6/2026, 11:15:06 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_set = set(nums)
        expected_nums = list(range(1, n + 1))

        output = []

        for num in expected_nums:
            if num not in nums_set:
                output.append(num)

        return output