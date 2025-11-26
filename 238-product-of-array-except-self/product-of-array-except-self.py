class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            [1, 2, 3, 4]
        p: 1[1, 2, 6, 24]
        s:  [24, 24, 12, 4]1
        for index 0: 1*24 = 24
        for index 1: 1*12 = 12
        for index 2: 2*4 = 8
        for index 3: 6*1 = 6

        p, s = 1,1
        for n in range(nums):
            ans[n] = p
            p *= nums[n]

        for n in range(nums, -1):
            ans[n] *= s
            s *= nums[n] 
        """

        pre = 1
        suf = 1
        ans = [1]*len(nums)
        print(ans)

        for n in range(len(nums)):
            ans[n] *= pre
            pre *= nums[n]

        for k in range(len(nums)-1, -1, -1):
            ans[k] *= suf
            suf *= nums[k]

        return ans 