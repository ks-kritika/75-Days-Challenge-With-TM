class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=float('inf')
        profit=-1
        maxProfit = 0
        for i in prices:
            if i< buy :
                buy = i
            elif i > buy:
                profit = i-buy
                maxProfit =max(maxProfit, profit)
        return maxProfit