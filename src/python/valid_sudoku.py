# https://leetcode-cn.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxs = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = int(board[i][j])
                if rows[i][num-1] == 1:
                    return False
                else:
                    rows[i][num-1] = 1

                if cols[j][num-1] == 1:
                    return False
                else:
                    cols[j][num-1] = 1

                if boxs[int(i/3)*3+int(j/3)][num-1] == 1:
                    return False
                else:
                    boxs[int(i/3)*3+int(j/3)][num-1] = 1
        
        return True

