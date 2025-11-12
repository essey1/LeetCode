class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
          LR  
        1 2 3
    TB  8 9 4
        7 6 5
        """
        # Pre-allocating
        matrix = []
        for j in range(n):
            matrix.append([0]*n)
        
        left, right = 0, n-1
        top, bottom = 0, n-1
        counter = 1

        # loop until left doesn't cross right
        while left <= right:

            # moving from left to right
            for c in range(left, right+1):
                matrix[top][c] = counter
                counter += 1
            top += 1

            # moving from top to bottom
            for r in range(top, bottom+1):
                matrix[r][right] = counter
                counter += 1
            right -= 1

            # moving from right to left
            for c in range(right, left-1, -1):
                matrix[bottom][c] = counter
                counter += 1
            bottom -= 1

            # moving from bottom to top
            for r in range(bottom, top-1, -1):
                matrix[r][left] = counter
                counter += 1
            left += 1

        return matrix
