# Last updated: 7/17/2026, 11:57:59 AM
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        output = []

        for i in range(1, n+1):
            if i%5==0 and i%3==0:
                output.append("FizzBuzz")
            elif i%3==0 and not i%5==0:
                output.append("Fizz")
            elif  i%5==0 and not i%3==0:
                output.append("Buzz")
            else:
                output.append(str(i))

        return output
            
        