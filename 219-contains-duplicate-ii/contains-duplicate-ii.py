class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashn = {}
         
        for i, val in enumerate(nums):
            if val in hashn and abs(i - hashn[val]) <=k:
                return True
            hashn[val] = i
        return False