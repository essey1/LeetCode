class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r, c = len(dungeon), len(dungeon[0])
        row = [float('inf')] * (c+1)
        row[c-1] = 1
        for i in range(r-1, -1, -1):
            newRow = [float('inf')] * (c+1)
            for j in range(c-1, -1, -1):
                next = min(newRow[j+1], row[j])
                newRow[j] = max(1, next - dungeon[i][j])
            row = newRow
        return row[0]

        