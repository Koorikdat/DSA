# Last updated: 8/6/2026, 11:15:22 PM
class Solution:
    def mySqrt(self, x: int) -> int:

        if x == None or x == 0:
            return 0
            
        elif x == 1:
            return 1


        i = 0
        
        while i <= x:
            sum = i * i
            if sum > x:
                return i-1
            else:
                i += 1