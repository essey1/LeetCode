class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # # sort: O(m*nlogn)
        # j = len(s1)
        # for i in range(len(s2)-len(s1)+1):
        #     s3 = s2[i:j]
        #     j += 1
        #     s3s = sorted(s3)
        #     s1s = sorted(s1)
        #     if s3s == s1s:
        #         return True
        # return False        

        # Array of size 26
        s1_arr = [0] * 26
        window = [0] * 26
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            s1_arr[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        j = 0
        for i in range(len(s1), len(s2)):
            if s1_arr == window:
                return True
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[j]) - ord('a')] -= 1
            j += 1
        if s1_arr == window:
                return True
        return False

        