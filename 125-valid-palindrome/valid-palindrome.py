class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = []
        
        for c in s:
            if c.isalnum():
                new_s.append(c)
        
        left = 0
        right = len(new_s) - 1
        print(new_s)
        while left < right:
            if new_s[left] == new_s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        
        