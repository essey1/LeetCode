class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:

        # Prefix Sum
        p_mat = [[0 for _ in range(len(mat[0])+1)] for _ in range(len(mat)+1)]
        # prefix sum matrix
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                # prefix += left + top - overlap
                p_mat[r+1][c+1] += mat[r][c] + p_mat[r][c+1] + p_mat[r+1][c] - p_mat[r][c]

        # Binary Search
        res = 0
        l, r = 0, min(len(mat), len(mat[0]))
        while l<=r:
            mid = (l+r)//2
            valid_square = False
            for i in range(mid-1, len(mat)):
                for j in range(mid-1, len(mat[0])):
                    summ = p_mat[i+1][j+1] + p_mat[i-mid+1][j-mid+1] - p_mat[i-mid+1][j+1] - p_mat[i+1][j-mid+1]
                    if summ <= threshold:
                        valid_square = True
                        break
                if valid_square:
                    break
            if valid_square:
                res = mid
                l = mid+1
            else:
                r = mid-1
        return res
        