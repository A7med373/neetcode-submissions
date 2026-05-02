class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # Brute Force
        """max_profit = 0
        for i in range(n):
            for j in range(i, n):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit"""
        # Two Pointers
        l, r = 0, 1
        max_profit = 0
        while r < n:
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_profit 
        # Dynamic Programming