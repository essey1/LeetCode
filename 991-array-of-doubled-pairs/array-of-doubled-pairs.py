class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # freq hashmap
        freq = defaultdict(int)
        for i in arr:
            freq[i] += 1

        # sort in abs value
        arr.sort(key=abs)
        print(arr)

        # check for pairs
        for i in range(len(arr)):
            num = arr[i]
            num2 = num*2

            if freq[num] == 0:
                continue

            if num2 not in freq or freq[num2]==0:
                return False
                
            freq[num2] -= 1
            freq[num] -= 1
        return True

        