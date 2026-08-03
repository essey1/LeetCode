class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        mid we're trying to find
        if nums[mid+1] < nums[mid] < nums[mid-1], min is found
        """
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid+1
            else:
                return nums[mid]
        