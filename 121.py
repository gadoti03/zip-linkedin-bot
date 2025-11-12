class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = inf
        profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > profit:
                profit = p - min_price
        return profit