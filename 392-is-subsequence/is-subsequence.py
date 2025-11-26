class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        for c in t:
            if j<len(s) and s[j] == c:
                j+=1

        if j == len(s):
            return True
        return False