class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # nums.sort()
        # j=1
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[j]:
        #         return True
        #     j += 1
        # return False

        numh = defaultdict(int)

        for i in nums:
            numh[i] += 1
            if numh[i] > 1:
                return True

        return False
        


