class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = [float('inf')] * (n+1)
        res[n-1] = 0

        for i in range(m-1, -1, -1):
            newRes = [float('inf')] * (n+1)
            for j in range(n-1, -1, -1):
                newRes[j] = grid[i][j] + min(res[j], newRes[j+1])
            res = newRes
        return res[0]

        