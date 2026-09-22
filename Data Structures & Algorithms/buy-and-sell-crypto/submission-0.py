class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprice=0
        for price in prices:
            minprice=min(minprice,price)
            maxprice=max(maxprice,price-minprice)
        return maxprice