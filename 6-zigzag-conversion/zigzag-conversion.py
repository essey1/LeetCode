class Solution:
    def convert(self, s: str, numRows: int) -> str:
        hashs = defaultdict(str)
        if numRows >= len(s):
            return s
        counter = 1
        for i in range(len(s)):
            hashs[counter] += s[i]
            if counter == 1:
                add = True
                counter += 1
            elif counter == numRows:
                add = False
                counter -= 1
            elif add == True:
                counter += 1
            else:
                counter -= 1
            print(counter)
        return "".join(hashs.values())
            