class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i, I in enumerate(s):
            if len(s) <= 1:
                res = s
                return res
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                temp = s[l:r+1]
                if len(temp) > len(res):
                    res = temp
                l -= 1
                r += 1 
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                temp = s[l:r+1]
                if len(temp) > len(res):
                    res = temp
                l -= 1
                r += 1 
        return res



        