class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)

        MAX = (2**31)-1
        MIN = -2**31
        for i in range(len(str(x))):
            dig = x % 10
            x //= 10

            if rev > (MAX-dig)//10:
                return 0
            rev = rev*10 + dig

        
        return rev*sign