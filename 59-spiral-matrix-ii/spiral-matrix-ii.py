class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
            L ->   R
          T 1 2 3 4
          T 0 0 0 0
            0 0 0 0
          B 0 0 0 0

          When moving horizontally the left and right pointers will tell
            us the range and top and bottom pointer will tell us which row to fill in

        When moving vertically the top and bottom pointers will tell
            us the range and right and left pointer will tell us which row to fill in
        """

        matrix = [[0] * n for _ in range(n)]
        l = 0
        right = n-1
        t = 0
        b = n-1
        counter = 1

        while t <= b:
            # fill in top row
            for c in range(l, right+1):
                matrix[t][c] = counter
                counter += 1
            t += 1

            # fill in the right column
            for r in range(t, b+1):
                matrix[r][right] = counter
                counter +=1
            right -= 1

            # fill in the bottom row (reverse)
            for c in range(right, l-1, -1):
                matrix[b][c] = counter
                counter += 1
            b -= 1

            # fill in the left column (reverse)
            for r in range(b, t-1, -1):
                matrix[r][l] = counter
                counter += 1
            l += 1

        return matrix