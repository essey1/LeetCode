class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        """
         LR  
        1 2 3
     TB 4 5 6
        7 8 9

      do these steps while left is less than or equal to right:
      move from left to right, increment top
      move from top to bottom, decrementing right
      move from right to left, decrement bottom
      move from bottom to top, increment left 
        """
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        top = 0
        right = n-1
        bottom = m-1
        print(right)
        print(bottom)
        output = []
        # Pre-allocating
        # for row in range(m):
        #     for col in range(n):
        #         output.append(0)  
        
        while left<=right:
            # move to the right
            if left>right:
                break
            for c in range(left, right+1):
                output.append(matrix[top][c])
            top += 1
            # move to the bottom
            if top>bottom:
                break
            for r in range(top, bottom+1):
                output.append(matrix[r][right])
            right -= 1
            # move to the left
            if left>right:
                break
            for c in range(right, left-1, -1):
                output.append(matrix[bottom][c])
            bottom -= 1
            # move to the top
            if top>bottom:
                break
            for r in range(bottom, top-1, -1):
                output.append(matrix[r][left])
            left += 1

        return output
        