class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        out=n
        while True:
            temp = out
            prd = 1
            while temp>0:
                digit = temp%10
                if digit == 0:
                    prd = 0
                    break
                prd *= digit
                temp //=10

            if prd % t == 0:
                return out
            else:
                out+=1 
            