class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Hashmap Approach

        # hn = defaultdict(int)
        # for i in nums:
        #     hn[i] +=1
        
        # res = 0
        # for i, _ in hn.items():
        #     if i+1 in hn:
        #         summ = hn[i]+hn[i+1]
        #         res = max(summ, res)

        # return res

        # Two Pointer Approach
        nums.sort()
        j = 0
        res = 0
        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            
            if nums[i] - nums[j] == 1:
                res = max(res, i-j+1)

        return res



            
        