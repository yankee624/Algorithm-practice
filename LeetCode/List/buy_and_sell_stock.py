from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price # minimum price until current time
            max_profit = max(price - min_price, max_profit)
        return max_profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))