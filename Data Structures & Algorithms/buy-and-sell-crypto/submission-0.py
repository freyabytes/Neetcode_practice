class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointers
        l=0 # buy index
        r=1 # Sell index
        maxProfit =0 # Maximum profit

        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxProfit=max(maxProfit,profit)
            else:
                l=r
            r+=1
        return maxProfit