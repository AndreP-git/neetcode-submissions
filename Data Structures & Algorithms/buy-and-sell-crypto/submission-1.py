class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        left = 0

        for right in range(len(prices)):
            profit = prices[right] - prices[left]

            if prices[right] < prices[left]:
                left = right
            
            max_profit = max(max_profit, profit) 
        
        return max_profit