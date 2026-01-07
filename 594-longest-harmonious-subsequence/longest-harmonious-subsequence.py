class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hn = defaultdict(int)
        for i in nums:
            hn[i] +=1
        
        res = 0
        for i, _ in hn.items():
            if i+1 in hn:
                summ = hn[i]+hn[i+1]
                res = max(summ, res)

        return res

            
        