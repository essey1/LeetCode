class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = 0
        ans = 0
        for i in piles:
            high = max(high, i)
        while low <= high:
            mid = (low+high)//2
            hr = 0
            for i in piles:
                if i <= mid:
                    hr += 1
                else:
                    hr = hr + -(i//-mid)
            if hr > h:
                low = mid+1
            else:
                ans = mid
                high = mid-1
        return ans

            

        