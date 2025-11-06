class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqMap = {}
        for num in arr:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        hashSet = set()
        for num in list(freqMap.values()):
            if num in hashSet:
                return False
            else:
                hashSet.add(num)
        return True
        print(list(freqMap.values()))