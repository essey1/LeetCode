class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        hashset = set()
        for i in list(freq.values()):
            if i in hashset:
                return False
            else:
                hashset.add(i)

        return True

