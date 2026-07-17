# Last updated: 7/17/2026, 11:57:50 AM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        arr = prices
        end = len(prices)
        
        for i in range (0,end):
            for j in range (i+1, end):

                if prices[j] <= prices[i]:

                    arr[i] = (prices[i] - prices[j])
                    break



            
        return (arr)

