class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        row = [0] * m
        row[m-1] = 1
        for i in range(n-1, -1, -1):
            newRow = [0] * m
            for j in range(m-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    newRow[j] = 0
                else:
                    right = newRow[j+1] if j+1 <= m-1 else 0
                    bottom = row[j]
                    newRow[j] = right + bottom
            row = newRow
        return newRow[0]
        