class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        out=n
        while True:
            prd = 1
            for c in str(out):
               prd *= int(c)
            if prd%t == 0:
                return out
            else:
                out += 1 
        