class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        hm = defaultdict(list)

        for s in (strs):
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")] += 1
            hm[tuple(count)].append(s)          

        for k, v in hm.items():
            output.append(v)
        return output

        