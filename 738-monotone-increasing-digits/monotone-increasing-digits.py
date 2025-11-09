class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # check if it's monotone 
        # if not decrement by one and check again

        
        digits = [int(d) for d in str(n)]
        monotone = True
        for i in range(len(digits)-1):
            if digits[i] > digits[i+1]:
                monotone  = False
                while i>0:
                    if digits[i-1] >= digits[i]:
                        i-=1
                    else:
                        break
                digits[i] -= 1
                print(digits)
                for j in range(i+1, len(digits)):
                    digits[j] = 9
                n = int(''.join(map(str, digits)))
                return n 
        if monotone:
            return n
            