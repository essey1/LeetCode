class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # sort both and check for equality
        # # O(nlogn)
        # s = sorted(s)
        # t = sorted(t)
        # if s == t:
        #     return True
        # else:
        #     return False

        # use counter dictionary 
        if len(s) != len(t):
            return False

        freq = {}
        # count characters in s
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        
        for c in t:
            if c not in freq:
                return False
            else:
                freq[c] -= 1
                if freq[c] < 0:
                    return False

        # for k in freq:
        #     if freq[k] != 0:
        #         return False

        return True