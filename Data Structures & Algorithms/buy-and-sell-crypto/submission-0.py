class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float("inf")
        max_profit = 0

        for i in range(0, len(prices)):
            min_val = min(min_val, prices[i])
            max_profit = max(max_profit,prices[i]-min_val)
        return max_profit
            
