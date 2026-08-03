class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        j=1
        for i in range(len(nums)-1):
            if nums[i] == nums[j]:
                return True
            j += 1
        return False
