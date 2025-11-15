class Solution:
    def firstUniqChar(self, s: str) -> int:
        sHash = {}
        for char in s:
            if char not in sHash:
                sHash[char] = 1
            else:
                sHash[char] += 1
        print(sHash)
        for i in range(len(s)):
            char = s[i]
            if sHash[char] == 1:
                return i
        return -1