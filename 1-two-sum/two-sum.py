class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Initiate a hashmap
        loop over the array nums
        for each n in nums:
            check if difference (target - current) exists in hashmap
            if it does return the key of hashmap and current
            if not add the nums value as key and index as value
        """
        hashn = {}
        for n in range(len(nums)):
            comp = target - nums[n]
            if comp in hashn:
                return [n, hashn[comp]]
            hashn[nums[n]] = n
