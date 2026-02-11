class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0

        l=0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                out = max(out, prices[r] - prices[l])
            else:
                l=r
        return out