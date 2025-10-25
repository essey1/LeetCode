class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        """
        res = []
        nums.sort()
        for i in range(len(nums)-1):
            left, right = i+1, len(nums)-1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while (left < right):
                if nums[left]+nums[right]+nums[i] > 0:
                    right -= 1
                elif nums[left]+nums[right]+nums[i] < 0:
                    left += 1
                elif nums[left]+nums[right]+nums[i] == 0:
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    right -= 1   
        return res
        