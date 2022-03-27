class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice , profit = float('inf') , 0
        
        for i in range ( len(prices) ):
            if prices[i] > buyprice:
                profit += prices[i] - buyprice
            buyprice=prices[i]
            
        return profit    