class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=0
        cp=0
        l=0
        while l<len(prices):
            cp=max(prices[l:len(prices)])-prices[l]
            mp=max(mp,cp)
            l+=1
        return mp