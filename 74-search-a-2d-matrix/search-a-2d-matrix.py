class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1. do a two binary searches
          - binary search over rows to find the row of target
          - binary search over the columns in that row
        2. use modulo operator
        """
        n = len(matrix)
        m = len(matrix[0])
        low_r = 0
        low_c = 0
        high_r = n-1
        high_c = m-1
        mid_r = 0
        while low_r <= high_r:
            mid = (low_r + high_r)//2
            if matrix[mid][0] <= target <= matrix[mid][m-1]:
                mid_r = mid
                break
            elif matrix[mid][m-1] < target:
                low_r = mid+1
            else:
                high_r = mid-1
        else:
            return False

        while low_c <= high_c:
            mid = (low_c + high_c)//2
            if target == matrix[mid_r][mid]:
                return True
            elif matrix[mid_r][mid] < target:
                low_c = mid+1
            else:
                high_c = mid-1
        return False



