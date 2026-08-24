class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_p = prices[0]
        max_profit = 0
        for i in prices:
            if i < min_p:
                min_p = i
            c_profit = i - min_p
            if c_profit > max_profit:
                max_profit = c_profit
        return max_profit