class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        j = len(s1)
        for i in range(len(s2)-len(s1)+1):
            s3 = s2[i:j]
            j += 1
            s3s = sorted(s3)
            s1s = sorted(s1)
            if s3s == s1s:
                return True
        return False        