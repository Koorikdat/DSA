# Last updated: 7/20/2026, 1:37:24 PM
class Solution:
    def sumAndMultiply(self, n: int) -> int:

        if n == 0:
            return 0


        n = str(n)
        x = ""
        sum = 0

        for i in n:
            if int(i) != 0:
                x += i
                sum += int(i)

        return(int(x)*sum)

        