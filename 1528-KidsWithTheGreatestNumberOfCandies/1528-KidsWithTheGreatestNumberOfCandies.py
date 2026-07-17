# Last updated: 7/17/2026, 11:57:51 AM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max = 0
        out = []

        for x in candies:
            if x > max:
                max = x

        for x in candies:
            if x + extraCandies >= max:
                out.append(True)
            else:
                out.append(False)

        
        print(out)
        return out

        