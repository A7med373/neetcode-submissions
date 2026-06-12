class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices) - 1
        # Brute Force
        max_profit = -float('inf')
        for i in range(n):
            for j in range(i, n):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit
        # Two Pointers
        # Dynamic Programming