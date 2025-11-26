class Solution:
    def reverse(self, x: int) -> int:
        """
        max = 50
        rev = 5
        dig = 2
        52
        48
        """
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

            if rev * 10 + dig <= MAX:
                rev = rev*10 + dig
            else:
                return 0

        
        return rev*sign