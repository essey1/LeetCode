class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[0:k])
        new_sum = summ
        for n in range(k, len(nums)):
            new_sum = new_sum + nums[n] - nums[n-k]
            summ = max(summ, new_sum)

        max_ave = summ/k
        return max_ave