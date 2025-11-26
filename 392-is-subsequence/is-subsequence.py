class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        counter = 0
        for i, c in enumerate(t):
            if j<len(s) and s[j] == c:
                j+=1
                counter+=1
            else: 
                continue

        if counter == len(s):
            return True
        return False