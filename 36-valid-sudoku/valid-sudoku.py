class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        conditions:
        no duplicates in row
        no duplicates in column
        no duplicates in sub 3x3 boxes
        """

        """
        approach:
        check row:
        curr = board[i][j]
        for i in board
            for j in board


        """
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        for r in range(9):
            seen = set()
            for c in range(9):
                if board[c][r] == ".":
                    continue
                if board[c][r] in seen:
                    return False
                seen.add(board[c][r])

        boxes = {}
        for r in range(9):
            for c in range(9):
                box_id = (r//3, c//3)
                if board[r][c] == ".":
                    continue
                if box_id not in boxes:
                    boxes[box_id] = set()
                if board[r][c] in boxes[box_id]:
                    return False
                boxes[box_id].add(board[r][c])
                


        return True
