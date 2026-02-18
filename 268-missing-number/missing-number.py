class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set(nums)
        arr = []

        for i in range(len(nums)+1):
            arr.append(i)
        for i in arr:
            if i not in nums:
                return i
        