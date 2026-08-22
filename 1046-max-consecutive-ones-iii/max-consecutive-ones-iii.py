class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        ans=0
        while r < len(nums):
            if nums[r] == 0 and k>0:
                k -= 1
                r += 1
            elif nums[r] == 1:
                r += 1
            else:
                if nums[l] == 0:
                    l += 1
                    k += 1
                else:
                    l += 1
            ans = max(ans, r-l)
        return ans

                        