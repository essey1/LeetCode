class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        rotate outer layer if the matric and then move in to the next
        """

        l = 0
        r = len(matrix) - 1

        while l < r:
            for i in range(0, r-l):
                t = l
                b = r

                #save topleft
                tl = matrix[t][l+i]

                matrix[t][l+i] = matrix[b-i][l]

                matrix[b-i][l] = matrix[b][r-i]
                
                matrix[b][r-i] = matrix[t+i][r]
                
                matrix[t+i][r] = tl

            r -= 1
            l += 1
        return matrix
            
        