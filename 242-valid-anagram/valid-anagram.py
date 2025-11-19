class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort both and check for equality
        # O(nlogn)
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False