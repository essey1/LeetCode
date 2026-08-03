class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high)//2
            hours = 0
            for p in piles:
                hours = hours + (p//mid)
                if p%mid != 0:
                    hours += 1
            if hours > h:
                low = mid+1
            else:
                ans = mid
                high = mid-1
        return ans     
        