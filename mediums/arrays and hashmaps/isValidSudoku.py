'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
'''
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board) :
        col  = defaultdict(set)
        rows = defaultdict(set)
        box = defaultdict(set)
        for rowI in range(9):
            for colI in range(9):
                if board[rowI][colI] == '.':
                    continue
                if (board[rowI][colI] in rows[rowI] or 
                board[rowI][colI] in col[colI] or 
                board[rowI][colI] in box[(rowI//3, colI//3)]):
                    return False
                rows[rowI].add(board[rowI][colI])  
                col[colI].add(board[rowI][colI])
                box[(rowI//3, colI//3)].add(board[rowI][colI])
        return True
sol = Solution()
sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])