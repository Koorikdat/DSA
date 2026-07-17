# Last updated: 7/17/2026, 11:57:58 AM
class Solution:
    def arrangeCoins(self, n: int) -> int:

        boxes = n

        for i in range (1, n + 1):
            if n == 1:
                return 1
            boxes = boxes - i
            if boxes < 0:
                return i - 1

                
        