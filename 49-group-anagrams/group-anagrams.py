class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        hm = defaultdict(list)

        for i, s in enumerate(strs):
            ss = "".join(sorted(s))
            if ss in hm:
                hm[ss].append(s)
            else:
                hm[ss].append(s)
        print(hm)

        for k, v in hm.items():
            output.append(v)
        return output

        