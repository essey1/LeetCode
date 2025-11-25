class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force O(n^2) nested loop
        # more optimal solution with two pointers
        """
        7 , 1 , 5 , 6 , 4
                        lr

        while r<len prices:
            if price of l < price of r:
                output = max(price[r] - price[l], output)
                r += 1
            else:
                l = r
                r+=1
        return ouput
        """
        l, r  = 0, 1
        max_profit = 0

        while r<len(prices):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1

        return max_profit