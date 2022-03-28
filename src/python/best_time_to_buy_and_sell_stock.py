# leetcode 121
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 99999
        result = 0
        length = len(prices)

        if length == 1:
            return 0

        for price in prices:
            result = max(result, price - minPrice)
            minPrice = min(minPrice, price)
        
        return result