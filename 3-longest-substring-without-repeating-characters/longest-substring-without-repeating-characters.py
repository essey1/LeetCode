class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        length = 0
        j=0
        for i in range(len(s)):
            freq[s[i]] += 1
            while freq[s[i]] > 1:
                freq[s[j]] -= 1
                j += 1
            length = max(length, i-j+1)
        return length


        